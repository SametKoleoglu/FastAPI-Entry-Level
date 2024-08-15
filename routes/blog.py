from fastapi import APIRouter
from models.blog import *
from config.config import blogs_collection
from serializers.blog import *
import datetime
from bson import ObjectId

blog_root = APIRouter()


# post request
@blog_root.post("/new/blog")
def new_blog(blog: BlogModel):
    blog = dict(blog)
    current_date = datetime.date.today()
    blog["date"] = str(current_date)

    response = blogs_collection.insert_one(blog)
    blog_id = str(response.inserted_id)

    return {"status": "OK", "message": "blog created successfully", "id": str(blog_id)}


# getting blogs
@blog_root.get("/blogs/")
def get_blogs():
    response = blogs_collection.find({})
    decoded_data = DecodeBlogs(response)

    return {"status": "OK", "data": decoded_data}


@blog_root.get("/blog/{blog_id}")
def get_blog(blog_id:str):
    response = blogs_collection.find_one({"_id": ObjectId(blog_id)})
    if not response:
        return {"status": "error", "message": "blog not found"}
   
    decoded_blog= DecodeBlog(response)

    return {"status": "OK", "data": decoded_blog}

@blog_root.delete("/blog/{blog_id}")
def delete_blog(blog_id:str):
    response = blogs_collection.delete_one({"_id": ObjectId(blog_id)})
    if response.deleted_count == 0:
        return {"status": "error", "message": "blog not found"}

    return {"status": "OK", "message": "blog deleted successfully"}


@blog_root.patch("/blog/{blog_id}")
def update_blog(blog_id:str, blog: UpdateBlogModel):
    req = dict(blog.model_dump(exclude_unset=True))
    
    blogs_collection.find_one_and_update({"_id": ObjectId(blog_id)}, {"$set": req})
    
    return {
        "status": "OK",
        "message": "blog updated successfully",
    }