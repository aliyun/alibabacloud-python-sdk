# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class FieldCondition(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        nest_field_path: str = None,
        nest_field_value: List[int] = None,
        operate_type: str = None,
        value: str = None,
    ):
        # 字段名称
        self.field_name = field_name
        # 复杂查询下，嵌套子条件字段jsonPath
        self.nest_field_path = nest_field_path
        # 复杂查询下，嵌套子条件字段值
        self.nest_field_value = nest_field_value
        # 操作符，枚举值
        self.operate_type = operate_type
        # 字段值，不同字段值类型不一样
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_name is not None:
            result['fieldName'] = self.field_name
        if self.nest_field_path is not None:
            result['nestFieldPath'] = self.nest_field_path
        if self.nest_field_value is not None:
            result['nestFieldValue'] = self.nest_field_value
        if self.operate_type is not None:
            result['operateType'] = self.operate_type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldName') is not None:
            self.field_name = m.get('fieldName')
        if m.get('nestFieldPath') is not None:
            self.nest_field_path = m.get('nestFieldPath')
        if m.get('nestFieldValue') is not None:
            self.nest_field_value = m.get('nestFieldValue')
        if m.get('operateType') is not None:
            self.operate_type = m.get('operateType')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ProductInstance(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        buyer_name: str = None,
        buyer_uid: str = None,
        channel: str = None,
        config: str = None,
        end: int = None,
        instance_id: str = None,
        order_no: str = None,
        product_code: str = None,
        product_spec_code: str = None,
        start: int = None,
        tenant_name: str = None,
        tenant_uid: str = None,
    ):
        # 应用码
        self.app_code = app_code
        # 购买者名称
        self.buyer_name = buyer_name
        # 购买者账号uid
        self.buyer_uid = buyer_uid
        # 商业化渠道码
        self.channel = channel
        # 购买配置信息
        self.config = config
        # 生效结束时间
        self.end = end
        # 实例id
        self.instance_id = instance_id
        # 订单号，幂等使用
        self.order_no = order_no
        # 产品码
        self.product_code = product_code
        # 规格码
        self.product_spec_code = product_spec_code
        # 生效开始时间
        self.start = start
        # 租户名称
        self.tenant_name = tenant_name
        # 租户uid
        self.tenant_uid = tenant_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['appCode'] = self.app_code
        if self.buyer_name is not None:
            result['buyerName'] = self.buyer_name
        if self.buyer_uid is not None:
            result['buyerUid'] = self.buyer_uid
        if self.channel is not None:
            result['channel'] = self.channel
        if self.config is not None:
            result['config'] = self.config
        if self.end is not None:
            result['end'] = self.end
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.order_no is not None:
            result['orderNo'] = self.order_no
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.product_spec_code is not None:
            result['productSpecCode'] = self.product_spec_code
        if self.start is not None:
            result['start'] = self.start
        if self.tenant_name is not None:
            result['tenantName'] = self.tenant_name
        if self.tenant_uid is not None:
            result['tenantUid'] = self.tenant_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        if m.get('buyerName') is not None:
            self.buyer_name = m.get('buyerName')
        if m.get('buyerUid') is not None:
            self.buyer_uid = m.get('buyerUid')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('orderNo') is not None:
            self.order_no = m.get('orderNo')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('productSpecCode') is not None:
            self.product_spec_code = m.get('productSpecCode')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('tenantName') is not None:
            self.tenant_name = m.get('tenantName')
        if m.get('tenantUid') is not None:
            self.tenant_uid = m.get('tenantUid')
        return self


class SearchCondition(TeaModel):
    def __init__(
        self,
        ass_keyword_list: List[str] = None,
        at_author_name_list: List[str] = None,
        author_name_list: List[str] = None,
        comments_level: int = None,
        content_len_level: int = None,
        create_time_end: int = None,
        create_time_start: int = None,
        doc_content_sign: str = None,
        doc_id_list: List[str] = None,
        duplicate_removal: bool = None,
        emotion_type: int = None,
        enable_keyword_highlight: bool = None,
        exclude_at_author_name_list: List[str] = None,
        exclude_author_name_list: List[str] = None,
        exclude_host_name_list: List[str] = None,
        exclude_keyword_list: List[str] = None,
        exclude_keyword_list_in_title: List[str] = None,
        exclude_keyword_tag_ids: List[int] = None,
        exclude_media_library_id_list: List[str] = None,
        exclude_media_name_list: List[str] = None,
        exclude_media_type_list: List[str] = None,
        exclude_message_type_list: List[str] = None,
        field_conditions: List[FieldCondition] = None,
        has_image: bool = None,
        has_video: bool = None,
        host_name_list: List[str] = None,
        keyword_tag_ids: List[int] = None,
        likes_level: int = None,
        media_library_id_list: List[str] = None,
        media_name_list: List[str] = None,
        media_type_list: List[str] = None,
        message_type_list: List[str] = None,
        page_now: int = None,
        page_size: int = None,
        parent_doc_id: str = None,
        pos_keyword_list: List[str] = None,
        pos_keyword_list_in_title: List[str] = None,
        publish_time_end: int = None,
        publish_time_start: int = None,
        reads_level: int = None,
        relevance_level: int = None,
        repost_level: int = None,
        sort_by: str = None,
        sort_by_direction: str = None,
        topic_list: List[str] = None,
        update_time_end: int = None,
        update_time_start: int = None,
    ):
        # 搭配词
        self.ass_keyword_list = ass_keyword_list
        # 被@的用户名称
        self.at_author_name_list = at_author_name_list
        # 作者名称
        self.author_name_list = author_name_list
        # 评论级别，1：100以内，2：100-1k，3：1k-1w以内，4：1w-10w，5，10w+\
        self.comments_level = comments_level
        # 内容长度级别，1：100以内，2：100-1k，3：1k-1w以内，4：1w-10w，5，10w+\
        self.content_len_level = content_len_level
        # 抓取截止时间
        self.create_time_end = create_time_end
        # 抓取起始时间
        self.create_time_start = create_time_start
        # 文章签名
        self.doc_content_sign = doc_content_sign
        # 舆情文章唯一docId
        self.doc_id_list = doc_id_list
        # 是否去重
        self.duplicate_removal = duplicate_removal
        # 情感类型，1非负，-1负面
        self.emotion_type = emotion_type
        # 是否高亮关键词
        self.enable_keyword_highlight = enable_keyword_highlight
        # 排除被@的用户名称
        self.exclude_at_author_name_list = exclude_at_author_name_list
        # 排除作者名称
        self.exclude_author_name_list = exclude_author_name_list
        # 排除网站域名
        self.exclude_host_name_list = exclude_host_name_list
        # 排除词
        self.exclude_keyword_list = exclude_keyword_list
        # 标题排除词
        self.exclude_keyword_list_in_title = exclude_keyword_list_in_title
        # 排除关键词标签Id列表
        self.exclude_keyword_tag_ids = exclude_keyword_tag_ids
        # 排除媒体库id列表
        self.exclude_media_library_id_list = exclude_media_library_id_list
        # 排除媒体名称
        self.exclude_media_name_list = exclude_media_name_list
        # 排除媒体类型，枚举值
        self.exclude_media_type_list = exclude_media_type_list
        # 排除消息类型，枚举值
        self.exclude_message_type_list = exclude_message_type_list
        # 其他过滤条件
        self.field_conditions = field_conditions
        # 文章是否含有图片
        self.has_image = has_image
        # 是否含有视频
        self.has_video = has_video
        # 网站域名
        self.host_name_list = host_name_list
        # 关键词标签Id列表
        self.keyword_tag_ids = keyword_tag_ids
        # 点赞级别，1：100以内，2：100-1k，3：1k-1w以内，4：1w-10w，5，10w+\
        self.likes_level = likes_level
        # 媒体库id列表
        self.media_library_id_list = media_library_id_list
        # 媒体名称
        self.media_name_list = media_name_list
        # 媒体类型，枚举值
        self.media_type_list = media_type_list
        # 消息类型，枚举值
        self.message_type_list = message_type_list
        # 当前页
        self.page_now = page_now
        # 页大小
        self.page_size = page_size
        # 舆情父文章的docId，一般用于查看某篇文章的评论
        self.parent_doc_id = parent_doc_id
        # 关键词
        self.pos_keyword_list = pos_keyword_list
        # 标题关键词
        self.pos_keyword_list_in_title = pos_keyword_list_in_title
        # 截止发布时间
        self.publish_time_end = publish_time_end
        # 起始发布时间
        self.publish_time_start = publish_time_start
        # 阅读级别，1：100以内，2：100-1k，3：1k-1w以内，4：1w-10w，5，10w+\
        self.reads_level = reads_level
        # 相关性等级，1：低，2：中，3：高，4：低级别以上
        self.relevance_level = relevance_level
        # 转发级别，1：100以内，2：100-1k，3：1k-1w以内，4：1w-10w，5，10w+\
        self.repost_level = repost_level
        # 排序字段
        self.sort_by = sort_by
        # 指定正反向排序
        self.sort_by_direction = sort_by_direction
        # #话题
        self.topic_list = topic_list
        # 舆情文章截止更新时间
        self.update_time_end = update_time_end
        # 舆情文章起始更新时间
        self.update_time_start = update_time_start

    def validate(self):
        if self.field_conditions:
            for k in self.field_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ass_keyword_list is not None:
            result['assKeywordList'] = self.ass_keyword_list
        if self.at_author_name_list is not None:
            result['atAuthorNameList'] = self.at_author_name_list
        if self.author_name_list is not None:
            result['authorNameList'] = self.author_name_list
        if self.comments_level is not None:
            result['commentsLevel'] = self.comments_level
        if self.content_len_level is not None:
            result['contentLenLevel'] = self.content_len_level
        if self.create_time_end is not None:
            result['createTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['createTimeStart'] = self.create_time_start
        if self.doc_content_sign is not None:
            result['docContentSign'] = self.doc_content_sign
        if self.doc_id_list is not None:
            result['docIdList'] = self.doc_id_list
        if self.duplicate_removal is not None:
            result['duplicateRemoval'] = self.duplicate_removal
        if self.emotion_type is not None:
            result['emotionType'] = self.emotion_type
        if self.enable_keyword_highlight is not None:
            result['enableKeywordHighlight'] = self.enable_keyword_highlight
        if self.exclude_at_author_name_list is not None:
            result['excludeAtAuthorNameList'] = self.exclude_at_author_name_list
        if self.exclude_author_name_list is not None:
            result['excludeAuthorNameList'] = self.exclude_author_name_list
        if self.exclude_host_name_list is not None:
            result['excludeHostNameList'] = self.exclude_host_name_list
        if self.exclude_keyword_list is not None:
            result['excludeKeywordList'] = self.exclude_keyword_list
        if self.exclude_keyword_list_in_title is not None:
            result['excludeKeywordListInTitle'] = self.exclude_keyword_list_in_title
        if self.exclude_keyword_tag_ids is not None:
            result['excludeKeywordTagIds'] = self.exclude_keyword_tag_ids
        if self.exclude_media_library_id_list is not None:
            result['excludeMediaLibraryIdList'] = self.exclude_media_library_id_list
        if self.exclude_media_name_list is not None:
            result['excludeMediaNameList'] = self.exclude_media_name_list
        if self.exclude_media_type_list is not None:
            result['excludeMediaTypeList'] = self.exclude_media_type_list
        if self.exclude_message_type_list is not None:
            result['excludeMessageTypeList'] = self.exclude_message_type_list
        result['fieldConditions'] = []
        if self.field_conditions is not None:
            for k in self.field_conditions:
                result['fieldConditions'].append(k.to_map() if k else None)
        if self.has_image is not None:
            result['hasImage'] = self.has_image
        if self.has_video is not None:
            result['hasVideo'] = self.has_video
        if self.host_name_list is not None:
            result['hostNameList'] = self.host_name_list
        if self.keyword_tag_ids is not None:
            result['keywordTagIds'] = self.keyword_tag_ids
        if self.likes_level is not None:
            result['likesLevel'] = self.likes_level
        if self.media_library_id_list is not None:
            result['mediaLibraryIdList'] = self.media_library_id_list
        if self.media_name_list is not None:
            result['mediaNameList'] = self.media_name_list
        if self.media_type_list is not None:
            result['mediaTypeList'] = self.media_type_list
        if self.message_type_list is not None:
            result['messageTypeList'] = self.message_type_list
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.parent_doc_id is not None:
            result['parentDocId'] = self.parent_doc_id
        if self.pos_keyword_list is not None:
            result['posKeywordList'] = self.pos_keyword_list
        if self.pos_keyword_list_in_title is not None:
            result['posKeywordListInTitle'] = self.pos_keyword_list_in_title
        if self.publish_time_end is not None:
            result['publishTimeEnd'] = self.publish_time_end
        if self.publish_time_start is not None:
            result['publishTimeStart'] = self.publish_time_start
        if self.reads_level is not None:
            result['readsLevel'] = self.reads_level
        if self.relevance_level is not None:
            result['relevanceLevel'] = self.relevance_level
        if self.repost_level is not None:
            result['repostLevel'] = self.repost_level
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        if self.sort_by_direction is not None:
            result['sortByDirection'] = self.sort_by_direction
        if self.topic_list is not None:
            result['topicList'] = self.topic_list
        if self.update_time_end is not None:
            result['updateTimeEnd'] = self.update_time_end
        if self.update_time_start is not None:
            result['updateTimeStart'] = self.update_time_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assKeywordList') is not None:
            self.ass_keyword_list = m.get('assKeywordList')
        if m.get('atAuthorNameList') is not None:
            self.at_author_name_list = m.get('atAuthorNameList')
        if m.get('authorNameList') is not None:
            self.author_name_list = m.get('authorNameList')
        if m.get('commentsLevel') is not None:
            self.comments_level = m.get('commentsLevel')
        if m.get('contentLenLevel') is not None:
            self.content_len_level = m.get('contentLenLevel')
        if m.get('createTimeEnd') is not None:
            self.create_time_end = m.get('createTimeEnd')
        if m.get('createTimeStart') is not None:
            self.create_time_start = m.get('createTimeStart')
        if m.get('docContentSign') is not None:
            self.doc_content_sign = m.get('docContentSign')
        if m.get('docIdList') is not None:
            self.doc_id_list = m.get('docIdList')
        if m.get('duplicateRemoval') is not None:
            self.duplicate_removal = m.get('duplicateRemoval')
        if m.get('emotionType') is not None:
            self.emotion_type = m.get('emotionType')
        if m.get('enableKeywordHighlight') is not None:
            self.enable_keyword_highlight = m.get('enableKeywordHighlight')
        if m.get('excludeAtAuthorNameList') is not None:
            self.exclude_at_author_name_list = m.get('excludeAtAuthorNameList')
        if m.get('excludeAuthorNameList') is not None:
            self.exclude_author_name_list = m.get('excludeAuthorNameList')
        if m.get('excludeHostNameList') is not None:
            self.exclude_host_name_list = m.get('excludeHostNameList')
        if m.get('excludeKeywordList') is not None:
            self.exclude_keyword_list = m.get('excludeKeywordList')
        if m.get('excludeKeywordListInTitle') is not None:
            self.exclude_keyword_list_in_title = m.get('excludeKeywordListInTitle')
        if m.get('excludeKeywordTagIds') is not None:
            self.exclude_keyword_tag_ids = m.get('excludeKeywordTagIds')
        if m.get('excludeMediaLibraryIdList') is not None:
            self.exclude_media_library_id_list = m.get('excludeMediaLibraryIdList')
        if m.get('excludeMediaNameList') is not None:
            self.exclude_media_name_list = m.get('excludeMediaNameList')
        if m.get('excludeMediaTypeList') is not None:
            self.exclude_media_type_list = m.get('excludeMediaTypeList')
        if m.get('excludeMessageTypeList') is not None:
            self.exclude_message_type_list = m.get('excludeMessageTypeList')
        self.field_conditions = []
        if m.get('fieldConditions') is not None:
            for k in m.get('fieldConditions'):
                temp_model = FieldCondition()
                self.field_conditions.append(temp_model.from_map(k))
        if m.get('hasImage') is not None:
            self.has_image = m.get('hasImage')
        if m.get('hasVideo') is not None:
            self.has_video = m.get('hasVideo')
        if m.get('hostNameList') is not None:
            self.host_name_list = m.get('hostNameList')
        if m.get('keywordTagIds') is not None:
            self.keyword_tag_ids = m.get('keywordTagIds')
        if m.get('likesLevel') is not None:
            self.likes_level = m.get('likesLevel')
        if m.get('mediaLibraryIdList') is not None:
            self.media_library_id_list = m.get('mediaLibraryIdList')
        if m.get('mediaNameList') is not None:
            self.media_name_list = m.get('mediaNameList')
        if m.get('mediaTypeList') is not None:
            self.media_type_list = m.get('mediaTypeList')
        if m.get('messageTypeList') is not None:
            self.message_type_list = m.get('messageTypeList')
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('parentDocId') is not None:
            self.parent_doc_id = m.get('parentDocId')
        if m.get('posKeywordList') is not None:
            self.pos_keyword_list = m.get('posKeywordList')
        if m.get('posKeywordListInTitle') is not None:
            self.pos_keyword_list_in_title = m.get('posKeywordListInTitle')
        if m.get('publishTimeEnd') is not None:
            self.publish_time_end = m.get('publishTimeEnd')
        if m.get('publishTimeStart') is not None:
            self.publish_time_start = m.get('publishTimeStart')
        if m.get('readsLevel') is not None:
            self.reads_level = m.get('readsLevel')
        if m.get('relevanceLevel') is not None:
            self.relevance_level = m.get('relevanceLevel')
        if m.get('repostLevel') is not None:
            self.repost_level = m.get('repostLevel')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        if m.get('sortByDirection') is not None:
            self.sort_by_direction = m.get('sortByDirection')
        if m.get('topicList') is not None:
            self.topic_list = m.get('topicList')
        if m.get('updateTimeEnd') is not None:
            self.update_time_end = m.get('updateTimeEnd')
        if m.get('updateTimeStart') is not None:
            self.update_time_start = m.get('updateTimeStart')
        return self


class YuqingMessage(TeaModel):
    def __init__(
        self,
        author_avatar_url: str = None,
        author_followers_count: int = None,
        author_friends_count: int = None,
        author_id: str = None,
        author_name: str = None,
        author_statuses_count: int = None,
        author_verify_type: str = None,
        create_time: int = None,
        doc_content: str = None,
        doc_content_brief: str = None,
        doc_content_sign: str = None,
        doc_id: str = None,
        doc_self_content_sign: str = None,
        doc_title: str = None,
        doc_url: str = None,
        emotion_type: int = None,
        highlight_keywords: List[str] = None,
        media_type: str = None,
        message_type: str = None,
        parent_doc_id: str = None,
        publish_time: int = None,
        relevance_score: float = None,
        similar_number: int = None,
        weibo_comment_id: str = None,
        weibo_mid: str = None,
    ):
        # 作者头像地址
        self.author_avatar_url = author_avatar_url
        # 粉丝数
        self.author_followers_count = author_followers_count
        # 好友数
        self.author_friends_count = author_friends_count
        # 作者id
        self.author_id = author_id
        # 作者名称
        self.author_name = author_name
        # 发文数
        self.author_statuses_count = author_statuses_count
        # 作者认证类型
        self.author_verify_type = author_verify_type
        # 舆情文章被抓取的时间戳
        self.create_time = create_time
        # 文章正文内容
        self.doc_content = doc_content
        # 文章摘要
        self.doc_content_brief = doc_content_brief
        # 文章内容签名，如果是转发微博或者其他有父内容的doc，计算的是父文章的得分。一般用于去重，相同的doc_content_sign说明内容相同
        self.doc_content_sign = doc_content_sign
        # 文章唯一docId
        self.doc_id = doc_id
        # 文章自身的内容签名，转发微博计算的是转发内容的contentSign，与父微博无关
        self.doc_self_content_sign = doc_self_content_sign
        # 文章标题
        self.doc_title = doc_title
        # 原文地址
        self.doc_url = doc_url
        # 情感的正负面，-1代表负面，1代表非负面
        self.emotion_type = emotion_type
        # 命中的搜索词列表
        self.highlight_keywords = highlight_keywords
        # 媒体类型，枚举值
        self.media_type = media_type
        # 舆情消息类型:转发,评论/回复, 原文,群聊等
        self.message_type = message_type
        # 文章的父docId，如被转发的文章docId
        self.parent_doc_id = parent_doc_id
        # 舆情文章的发布时间戳
        self.publish_time = publish_time
        # 相关性得分
        self.relevance_score = relevance_score
        # 相似文章数
        self.similar_number = similar_number
        # 微博评论id
        self.weibo_comment_id = weibo_comment_id
        # 微博消息id
        self.weibo_mid = weibo_mid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_avatar_url is not None:
            result['authorAvatarUrl'] = self.author_avatar_url
        if self.author_followers_count is not None:
            result['authorFollowersCount'] = self.author_followers_count
        if self.author_friends_count is not None:
            result['authorFriendsCount'] = self.author_friends_count
        if self.author_id is not None:
            result['authorId'] = self.author_id
        if self.author_name is not None:
            result['authorName'] = self.author_name
        if self.author_statuses_count is not None:
            result['authorStatusesCount'] = self.author_statuses_count
        if self.author_verify_type is not None:
            result['authorVerifyType'] = self.author_verify_type
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.doc_content is not None:
            result['docContent'] = self.doc_content
        if self.doc_content_brief is not None:
            result['docContentBrief'] = self.doc_content_brief
        if self.doc_content_sign is not None:
            result['docContentSign'] = self.doc_content_sign
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.doc_self_content_sign is not None:
            result['docSelfContentSign'] = self.doc_self_content_sign
        if self.doc_title is not None:
            result['docTitle'] = self.doc_title
        if self.doc_url is not None:
            result['docUrl'] = self.doc_url
        if self.emotion_type is not None:
            result['emotionType'] = self.emotion_type
        if self.highlight_keywords is not None:
            result['highlightKeywords'] = self.highlight_keywords
        if self.media_type is not None:
            result['mediaType'] = self.media_type
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.parent_doc_id is not None:
            result['parentDocId'] = self.parent_doc_id
        if self.publish_time is not None:
            result['publishTime'] = self.publish_time
        if self.relevance_score is not None:
            result['relevanceScore'] = self.relevance_score
        if self.similar_number is not None:
            result['similarNumber'] = self.similar_number
        if self.weibo_comment_id is not None:
            result['weiboCommentId'] = self.weibo_comment_id
        if self.weibo_mid is not None:
            result['weiboMid'] = self.weibo_mid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorAvatarUrl') is not None:
            self.author_avatar_url = m.get('authorAvatarUrl')
        if m.get('authorFollowersCount') is not None:
            self.author_followers_count = m.get('authorFollowersCount')
        if m.get('authorFriendsCount') is not None:
            self.author_friends_count = m.get('authorFriendsCount')
        if m.get('authorId') is not None:
            self.author_id = m.get('authorId')
        if m.get('authorName') is not None:
            self.author_name = m.get('authorName')
        if m.get('authorStatusesCount') is not None:
            self.author_statuses_count = m.get('authorStatusesCount')
        if m.get('authorVerifyType') is not None:
            self.author_verify_type = m.get('authorVerifyType')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('docContent') is not None:
            self.doc_content = m.get('docContent')
        if m.get('docContentBrief') is not None:
            self.doc_content_brief = m.get('docContentBrief')
        if m.get('docContentSign') is not None:
            self.doc_content_sign = m.get('docContentSign')
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('docSelfContentSign') is not None:
            self.doc_self_content_sign = m.get('docSelfContentSign')
        if m.get('docTitle') is not None:
            self.doc_title = m.get('docTitle')
        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')
        if m.get('emotionType') is not None:
            self.emotion_type = m.get('emotionType')
        if m.get('highlightKeywords') is not None:
            self.highlight_keywords = m.get('highlightKeywords')
        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('parentDocId') is not None:
            self.parent_doc_id = m.get('parentDocId')
        if m.get('publishTime') is not None:
            self.publish_time = m.get('publishTime')
        if m.get('relevanceScore') is not None:
            self.relevance_score = m.get('relevanceScore')
        if m.get('similarNumber') is not None:
            self.similar_number = m.get('similarNumber')
        if m.get('weiboCommentId') is not None:
            self.weibo_comment_id = m.get('weiboCommentId')
        if m.get('weiboMid') is not None:
            self.weibo_mid = m.get('weiboMid')
        return self


class CloseProductRequest(TeaModel):
    def __init__(
        self,
        product_instance: ProductInstance = None,
        request_id: str = None,
    ):
        self.product_instance = product_instance
        # A short description of struct
        self.request_id = request_id

    def validate(self):
        if self.product_instance:
            self.product_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_instance is not None:
            result['productInstance'] = self.product_instance.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productInstance') is not None:
            temp_model = ProductInstance()
            self.product_instance = temp_model.from_map(m['productInstance'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CloseProductResponseBody(TeaModel):
    def __init__(
        self,
        data: int = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CloseProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CloseProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConsoleProxyRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        interface_name: str = None,
        param_json: str = None,
        request_id: str = None,
        team_hash_id: str = None,
    ):
        self.app_code = app_code
        self.interface_name = interface_name
        self.param_json = param_json
        # A short description of struct
        self.request_id = request_id
        self.team_hash_id = team_hash_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['appCode'] = self.app_code
        if self.interface_name is not None:
            result['interfaceName'] = self.interface_name
        if self.param_json is not None:
            result['paramJson'] = self.param_json
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        if m.get('interfaceName') is not None:
            self.interface_name = m.get('interfaceName')
        if m.get('paramJson') is not None:
            self.param_json = m.get('paramJson')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        return self


class ConsoleProxyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_json: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.result_json = result_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result_json is not None:
            result['resultJson'] = self.result_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resultJson') is not None:
            self.result_json = m.get('resultJson')
        return self


class ConsoleProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConsoleProxyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConsoleProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAnalysisTaskResultRequest(TeaModel):
    def __init__(
        self,
        analysis_id: int = None,
        request_id: str = None,
        team_hash_id: str = None,
    ):
        self.analysis_id = analysis_id
        # A short description of struct
        self.request_id = request_id
        self.team_hash_id = team_hash_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        return self


class GetAnalysisTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        analysis_id: int = None,
        request_id: str = None,
        result_json: str = None,
    ):
        self.analysis_id = analysis_id
        # Id of the request
        self.request_id = request_id
        self.result_json = result_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result_json is not None:
            result['resultJson'] = self.result_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resultJson') is not None:
            self.result_json = m.get('resultJson')
        return self


class GetAnalysisTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAnalysisTaskResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAnalysisTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenProductRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        product_instance: ProductInstance = None,
        request_id: str = None,
    ):
        # 幂等参数
        self.client_token = client_token
        self.product_instance = product_instance
        # A short description of struct
        self.request_id = request_id

    def validate(self):
        if self.product_instance:
            self.product_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.product_instance is not None:
            result['productInstance'] = self.product_instance.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('productInstance') is not None:
            temp_model = ProductInstance()
            self.product_instance = temp_model.from_map(m['productInstance'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class OpenProductResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class OpenProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProductInstanceListRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        from_time: int = None,
        request_id: str = None,
        tenant_uid: str = None,
        to_time: int = None,
    ):
        self.app_code = app_code
        self.from_time = from_time
        # A short description of struct
        self.request_id = request_id
        self.tenant_uid = tenant_uid
        self.to_time = to_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['appCode'] = self.app_code
        if self.from_time is not None:
            result['fromTime'] = self.from_time
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.tenant_uid is not None:
            result['tenantUid'] = self.tenant_uid
        if self.to_time is not None:
            result['toTime'] = self.to_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appCode') is not None:
            self.app_code = m.get('appCode')
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('tenantUid') is not None:
            self.tenant_uid = m.get('tenantUid')
        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')
        return self


class QueryProductInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        instance_list: List[ProductInstance] = None,
        request_id: str = None,
    ):
        self.instance_list = instance_list
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['instanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['instanceList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('instanceList') is not None:
            for k in m.get('instanceList'):
                temp_model = ProductInstance()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryProductInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryProductInstanceListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryProductInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryYuqingMessageRequest(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        search_condition: SearchCondition = None,
        team_hash_id: str = None,
    ):
        # A short description of struct
        self.request_id = request_id
        self.search_condition = search_condition
        self.team_hash_id = team_hash_id

    def validate(self):
        if self.search_condition:
            self.search_condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.search_condition is not None:
            result['searchCondition'] = self.search_condition.to_map()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('searchCondition') is not None:
            temp_model = SearchCondition()
            self.search_condition = temp_model.from_map(m['searchCondition'])
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        return self


class QueryYuqingMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        yuqing_messages: List[YuqingMessage] = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count
        self.yuqing_messages = yuqing_messages

    def validate(self):
        if self.yuqing_messages:
            for k in self.yuqing_messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['yuqingMessages'] = []
        if self.yuqing_messages is not None:
            for k in self.yuqing_messages:
                result['yuqingMessages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.yuqing_messages = []
        if m.get('yuqingMessages') is not None:
            for k in m.get('yuqingMessages'):
                temp_model = YuqingMessage()
                self.yuqing_messages.append(temp_model.from_map(k))
        return self


class QueryYuqingMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryYuqingMessageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryYuqingMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        analyse_type: str = None,
        request_id: str = None,
        search_condition: SearchCondition = None,
        team_hash_id: str = None,
    ):
        self.analyse_type = analyse_type
        # A short description of struct
        self.request_id = request_id
        self.search_condition = search_condition
        self.team_hash_id = team_hash_id

    def validate(self):
        if self.search_condition:
            self.search_condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analyse_type is not None:
            result['analyseType'] = self.analyse_type
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.search_condition is not None:
            result['searchCondition'] = self.search_condition.to_map()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyseType') is not None:
            self.analyse_type = m.get('analyseType')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('searchCondition') is not None:
            temp_model = SearchCondition()
            self.search_condition = temp_model.from_map(m['searchCondition'])
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        return self


class SubmitAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        analysis_id: int = None,
        request_id: str = None,
        result_json: str = None,
    ):
        self.analysis_id = analysis_id
        # Id of the request
        self.request_id = request_id
        self.result_json = result_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result_json is not None:
            result['resultJson'] = self.result_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resultJson') is not None:
            self.result_json = m.get('resultJson')
        return self


class SubmitAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitAnalysisTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


