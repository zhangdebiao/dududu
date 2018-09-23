#coding:utf-8
from django.db import models
from db.base_model import BaseModel
from users.models import Passport
from books.models import Books
# Create your models here.


class CommentsManager(models.Manager):
    '''评论模型管理器类'''
    # sort='new' 按照创建时间进行排序
    # sort='hot' 按照...进行排序
    # sort='rating' 按照商品的评分进行排序
    # sort= 按照默认顺序排序
    def get_comms_by_bookid(self, book_id, limit=None, sort='default'):
        '''根据评论类型id查询评论信息'''
        if sort == 'new':
            order_by = ('-create_time', )
        elif sort == 'hot':
            order_by = ('-update_time', )
        elif sort == 'rating':
            order_by = ('rating', )
        else:
            order_by = ('-pk', ) # 按照primary key降序排列。

        # 查询数据
        comms_li = self.filter(book_id=book_id).order_by(*order_by)

        # 查询结果集的限制
        if limit:
            comms_li = comms_li[:limit]
        return comms_li

    # def get_comms_by_id(self, book_id):
    #     '''根据评论的id获取评论信息'''
    #     try:
    #         comms = self.get(id=book_id)
    #     except self.model.DoesNotExist:
    #         # 不存在商品信息
    #         comms = None
    #     return comms



class Comments(BaseModel):
    disabled = models.BooleanField(default=False, verbose_name="禁用评论")
    user = models.ForeignKey('users.Passport', verbose_name="用户ID")
    book = models.ForeignKey('books.Books', verbose_name="书籍ID")
    content = models.CharField(max_length=1000, verbose_name="评论内容")
    title = models.CharField(max_length=20, verbose_name="评论标题", default="")
    rating = models.IntegerField(default=1, verbose_name="评分")

    #objects = models.Manager()
    objects = CommentsManager()

    class Meta:
        db_table = 's_comment_table'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

