# one blog


def DecodeBlog(blog) -> dict:
    return {
        "_id": str(blog["_id"]),
        "title": blog["title"],
        "sub_title": blog["sub_title"],
        "content": blog["content"],
        "author": blog["author"],
        "date": blog["date"],
    }


# all blogs
def DecodeBlogs(blogs) -> list:
    return [DecodeBlog(blog) for blog in blogs]
