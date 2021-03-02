# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class Project(TeaModel):
    def __init__(
        self,
        ass_keywords: str = None,
        default_filter_id: int = None,
        ext_criteria: str = None,
        id: int = None,
        name: str = None,
        neg_keywords: str = None,
        pid: int = None,
        pos_keywords: str = None,
        project_group_id: int = None,
        project_type: int = None,
        project_type_name: str = None,
        sub_project_ids: List[int] = None,
        team_id: int = None,
        valid: int = None,
        gmt_create_timestamp: int = None,
        gmt_modified_timestamp: int = None,
        uname_create: str = None,
        uid_create: str = None,
        uname_modified: str = None,
        uid_modified: str = None,
    ):
        # 搭配词
        self.ass_keywords = ass_keywords
        # 项目的默认过滤模板ID
        self.default_filter_id = default_filter_id
        # 高级用法，非关键词配置，如at用户，标题排除词。
        self.ext_criteria = ext_criteria
        # 舆情项目ID
        self.id = id
        # 项目名称
        self.name = name
        # 排除词
        self.neg_keywords = neg_keywords
        # 项目父ID，如果没有父项目则为0
        self.pid = pid
        # 项目关键词
        self.pos_keywords = pos_keywords
        # 项目归属分组ID，0代表没有分组
        self.project_group_id = project_group_id
        # 0:通用舆情项目，1：金融舆情项目
        self.project_type = project_type
        # 舆情项目类型名称
        self.project_type_name = project_type_name
        # 项目的子项目ID列表
        self.sub_project_ids = sub_project_ids
        # 团队id
        self.team_id = team_id
        # 状态，1为生效，0为失效。
        self.valid = valid
        # 项目创建时间，毫秒
        self.gmt_create_timestamp = gmt_create_timestamp
        # 项目修改时间，毫秒
        self.gmt_modified_timestamp = gmt_modified_timestamp
        # 项目创建人名称
        self.uname_create = uname_create
        # 项目创建人uid
        self.uid_create = uid_create
        # 项目修改人名称
        self.uname_modified = uname_modified
        # 项目修改人uid
        self.uid_modified = uid_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ass_keywords is not None:
            result['assKeywords'] = self.ass_keywords
        if self.default_filter_id is not None:
            result['defaultFilterId'] = self.default_filter_id
        if self.ext_criteria is not None:
            result['extCriteria'] = self.ext_criteria
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.neg_keywords is not None:
            result['negKeywords'] = self.neg_keywords
        if self.pid is not None:
            result['pid'] = self.pid
        if self.pos_keywords is not None:
            result['posKeywords'] = self.pos_keywords
        if self.project_group_id is not None:
            result['projectGroupId'] = self.project_group_id
        if self.project_type is not None:
            result['projectType'] = self.project_type
        if self.project_type_name is not None:
            result['projectTypeName'] = self.project_type_name
        if self.sub_project_ids is not None:
            result['subProjectIds'] = self.sub_project_ids
        if self.team_id is not None:
            result['teamId'] = self.team_id
        if self.valid is not None:
            result['valid'] = self.valid
        if self.gmt_create_timestamp is not None:
            result['gmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.uname_create is not None:
            result['unameCreate'] = self.uname_create
        if self.uid_create is not None:
            result['uidCreate'] = self.uid_create
        if self.uname_modified is not None:
            result['unameModified'] = self.uname_modified
        if self.uid_modified is not None:
            result['uidModified'] = self.uid_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assKeywords') is not None:
            self.ass_keywords = m.get('assKeywords')
        if m.get('defaultFilterId') is not None:
            self.default_filter_id = m.get('defaultFilterId')
        if m.get('extCriteria') is not None:
            self.ext_criteria = m.get('extCriteria')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('negKeywords') is not None:
            self.neg_keywords = m.get('negKeywords')
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        if m.get('posKeywords') is not None:
            self.pos_keywords = m.get('posKeywords')
        if m.get('projectGroupId') is not None:
            self.project_group_id = m.get('projectGroupId')
        if m.get('projectType') is not None:
            self.project_type = m.get('projectType')
        if m.get('projectTypeName') is not None:
            self.project_type_name = m.get('projectTypeName')
        if m.get('subProjectIds') is not None:
            self.sub_project_ids = m.get('subProjectIds')
        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        if m.get('gmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('gmtCreateTimestamp')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('unameCreate') is not None:
            self.uname_create = m.get('unameCreate')
        if m.get('uidCreate') is not None:
            self.uid_create = m.get('uidCreate')
        if m.get('unameModified') is not None:
            self.uname_modified = m.get('unameModified')
        if m.get('uidModified') is not None:
            self.uid_modified = m.get('uidModified')
        return self


class BizTagTree(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        gmt_modified_timestamp: int = None,
        id: int = None,
        name: str = None,
        parent_id: int = None,
        status: int = None,
        tag_id_path: str = None,
        tag_name_path: str = None,
        uid_create: str = None,
        uid_modified: str = None,
        uname_create: str = None,
        uname_modified: str = None,
    ):
        # 创建时间，毫秒
        self.gmt_create_timestamp = gmt_create_timestamp
        # 修改时间，毫秒
        self.gmt_modified_timestamp = gmt_modified_timestamp
        # 标签id
        self.id = id
        # 标签名字
        self.name = name
        # 父亲id
        self.parent_id = parent_id
        # 标签状态，1表示激活，0表示不激活
        self.status = status
        # 标签节点树
        self.tag_id_path = tag_id_path
        # 标签节点名字树
        self.tag_name_path = tag_name_path
        # 创建人id
        self.uid_create = uid_create
        # 修改人id
        self.uid_modified = uid_modified
        # 创建人名字
        self.uname_create = uname_create
        # 修改人名字
        self.uname_modified = uname_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['gmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.status is not None:
            result['status'] = self.status
        if self.tag_id_path is not None:
            result['tagIdPath'] = self.tag_id_path
        if self.tag_name_path is not None:
            result['tagNamePath'] = self.tag_name_path
        if self.uid_create is not None:
            result['uidCreate'] = self.uid_create
        if self.uid_modified is not None:
            result['uidModified'] = self.uid_modified
        if self.uname_create is not None:
            result['unameCreate'] = self.uname_create
        if self.uname_modified is not None:
            result['unameModified'] = self.uname_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('gmtCreateTimestamp')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tagIdPath') is not None:
            self.tag_id_path = m.get('tagIdPath')
        if m.get('tagNamePath') is not None:
            self.tag_name_path = m.get('tagNamePath')
        if m.get('uidCreate') is not None:
            self.uid_create = m.get('uidCreate')
        if m.get('uidModified') is not None:
            self.uid_modified = m.get('uidModified')
        if m.get('unameCreate') is not None:
            self.uname_create = m.get('unameCreate')
        if m.get('unameModified') is not None:
            self.uname_modified = m.get('unameModified')
        return self


class ReportNotifyRecord(TeaModel):
    def __init__(
        self,
        conf: str = None,
        cp_id: int = None,
        gmt_create_timestamp: int = None,
        gmt_create_format: str = None,
        gmt_modified_timestamp: int = None,
        id: int = None,
        share_key: str = None,
        subject: str = None,
        success: int = None,
        type: int = None,
        uid_create: str = None,
        uname_create: str = None,
        valid: int = None,
    ):
        # 配置： 如图片宽度/接收人/抄送人等
        self.conf = conf
        # 自定义页面id
        self.cp_id = cp_id
        # 创建时间，毫秒
        self.gmt_create_timestamp = gmt_create_timestamp
        # 格式化的创建时间
        self.gmt_create_format = gmt_create_format
        # 修改时间，毫秒
        self.gmt_modified_timestamp = gmt_modified_timestamp
        # 记录id
        self.id = id
        # cpId对应的共享key，用于共享报告
        self.share_key = share_key
        # 主题
        self.subject = subject
        # 是否成功的标志，1表示成功，否则表示不成功
        self.success = success
        # 类型： 如邮件、钉钉等
        self.type = type
        # 创建人id
        self.uid_create = uid_create
        # 创建人名字
        self.uname_create = uname_create
        # 状态，1为生效，0为失效。
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conf is not None:
            result['conf'] = self.conf
        if self.cp_id is not None:
            result['cpId'] = self.cp_id
        if self.gmt_create_timestamp is not None:
            result['gmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_create_format is not None:
            result['gmtCreateFormat'] = self.gmt_create_format
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.id is not None:
            result['id'] = self.id
        if self.share_key is not None:
            result['shareKey'] = self.share_key
        if self.subject is not None:
            result['subject'] = self.subject
        if self.success is not None:
            result['success'] = self.success
        if self.type is not None:
            result['type'] = self.type
        if self.uid_create is not None:
            result['uidCreate'] = self.uid_create
        if self.uname_create is not None:
            result['unameCreate'] = self.uname_create
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conf') is not None:
            self.conf = m.get('conf')
        if m.get('cpId') is not None:
            self.cp_id = m.get('cpId')
        if m.get('gmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('gmtCreateTimestamp')
        if m.get('gmtCreateFormat') is not None:
            self.gmt_create_format = m.get('gmtCreateFormat')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('shareKey') is not None:
            self.share_key = m.get('shareKey')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uidCreate') is not None:
            self.uid_create = m.get('uidCreate')
        if m.get('unameCreate') is not None:
            self.uname_create = m.get('unameCreate')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class SearchCondition(TeaModel):
    def __init__(
        self,
        project_id: int = None,
        filter_id: int = None,
        ass_keywords_idx: str = None,
        author_followers_count_max_filter: int = None,
        author_followers_count_min_filter: int = None,
        author_name_idx: str = None,
        author_verify_type_filter: str = None,
        comments_count_max_filter: int = None,
        comments_count_min_filter: int = None,
        content_length_max_filter: int = None,
        content_length_min_filter: int = None,
        doc_answers_count_max_filter: int = None,
        doc_answers_count_min_filter: int = None,
        doc_area_idx: str = None,
        doc_content_sign_idx: str = None,
        doc_create_time_end_filter: int = None,
        doc_create_time_start_filter: int = None,
        doc_publish_time_end_filter: int = None,
        doc_publish_time_start_filter: int = None,
        duplicate_removal: bool = None,
        emotion_score_max_filter: float = None,
        emotion_score_min_filter: float = None,
        exclude_author_name_idx: str = None,
        excluding_media_hosts_filter: str = None,
        excluding_media_pool_ids_filter: str = None,
        likes_count_max_filter: int = None,
        likes_count_min_filter: int = None,
        media_hosts_filter: str = None,
        media_influence_score_max_filter: float = None,
        media_influence_score_min_filter: float = None,
        media_pool_ids_filter: str = None,
        media_propagation_score_max_filter: float = None,
        media_propagation_score_min_filter: float = None,
        media_type_filter: str = None,
        message_type_filter: str = None,
        neg_keywords_idx: str = None,
        page_now: int = None,
        page_size: int = None,
        pos_keywords_idx: str = None,
        primary_key_idx: str = None,
        reads_count_max_filter: int = None,
        reads_count_min_filter: int = None,
        relevance_score_max_filter: float = None,
        relevance_score_min_filter: float = None,
        reposts_count_max_filter: int = None,
        reposts_count_min_filter: int = None,
        reprint_from_filter: str = None,
        title_excluding_words_idx: str = None,
        title_including_words_idx: str = None,
        used_index_mode_switch: str = None,
        eroticism_filter: bool = None,
        gambling_filter: bool = None,
        bkz_filter: bool = None,
        advertisement_filter: bool = None,
        illegal_advertisement_filter: bool = None,
        spam_filter: bool = None,
        suspicion_spam_filter: bool = None,
        biz_tags_idx: str = None,
        alipay_account_filter: str = None,
        doc_update_time_end_filter: int = None,
        doc_update_time_start_filter: int = None,
        enable_keyword_highlight: bool = None,
        finance_entity_area_filter: str = None,
        entity_name: str = None,
        finance_entity_relevance_score_max_filter: float = None,
        finance_entity_relevance_score_min_filter: float = None,
        finance_event_code_filter: str = None,
        parent_ids_idx: str = None,
        sort_by_direction: str = None,
        sort_by: str = None,
    ):
        # 舆情项目Id
        self.project_id = project_id
        # 舆情筛选模板Id
        self.filter_id = filter_id
        # 搭配词，json字符串数组
        self.ass_keywords_idx = ass_keywords_idx
        # 粉丝数上限
        self.author_followers_count_max_filter = author_followers_count_max_filter
        # 粉丝数下限
        self.author_followers_count_min_filter = author_followers_count_min_filter
        # 指定用户名，多个用户用英文逗号隔开
        self.author_name_idx = author_name_idx
        # 作者认证类型，多个用,隔开
        self.author_verify_type_filter = author_verify_type_filter
        # 评论数上限
        self.comments_count_max_filter = comments_count_max_filter
        # 评论数下限
        self.comments_count_min_filter = comments_count_min_filter
        # 内容长度上限
        self.content_length_max_filter = content_length_max_filter
        # 内容长度下限
        self.content_length_min_filter = content_length_min_filter
        # 答案数上限
        self.doc_answers_count_max_filter = doc_answers_count_max_filter
        # 答案数下限
        self.doc_answers_count_min_filter = doc_answers_count_min_filter
        # 提级地域
        self.doc_area_idx = doc_area_idx
        # 相似文章索引Id,，多个用英文逗号隔开
        self.doc_content_sign_idx = doc_content_sign_idx
        # 创建时间戳上限
        self.doc_create_time_end_filter = doc_create_time_end_filter
        # 创建时间戳下限
        self.doc_create_time_start_filter = doc_create_time_start_filter
        # 发布时间戳上限
        self.doc_publish_time_end_filter = doc_publish_time_end_filter
        # 发布时间戳下限
        self.doc_publish_time_start_filter = doc_publish_time_start_filter
        # 返回的数据是否去重，默认true
        self.duplicate_removal = duplicate_removal
        # 情感分值上限，范围-10~10
        self.emotion_score_max_filter = emotion_score_max_filter
        # 情感分值下限，范围-10~10
        self.emotion_score_min_filter = emotion_score_min_filter
        # 排除指定用户名，多个用户用英文逗号隔开
        self.exclude_author_name_idx = exclude_author_name_idx
        # 排除指定Host
        self.excluding_media_hosts_filter = excluding_media_hosts_filter
        # 排除指定媒体库ids，媒体库在舆情平台上定义
        self.excluding_media_pool_ids_filter = excluding_media_pool_ids_filter
        # 点赞数上限
        self.likes_count_max_filter = likes_count_max_filter
        # 点赞数下限
        self.likes_count_min_filter = likes_count_min_filter
        # 指定Host
        self.media_hosts_filter = media_hosts_filter
        # 媒体影响分上限
        self.media_influence_score_max_filter = media_influence_score_max_filter
        # 媒体影响分下限
        self.media_influence_score_min_filter = media_influence_score_min_filter
        # 指定媒体库ids，媒体库在舆情平台上定义
        self.media_pool_ids_filter = media_pool_ids_filter
        # 媒体传播分上限取值范围：0-10分
        self.media_propagation_score_max_filter = media_propagation_score_max_filter
        # 媒体传播分下限取值范围：0-10分
        self.media_propagation_score_min_filter = media_propagation_score_min_filter
        # 枚举字符串如：WEIBO-WEIBO
        self.media_type_filter = media_type_filter
        # 枚举字符串如：COMMENT
        self.message_type_filter = message_type_filter
        # 排除关键词
        self.neg_keywords_idx = neg_keywords_idx
        # 指定页码
        self.page_now = page_now
        # 指定每页大小，最大50
        self.page_size = page_size
        # 格式同AssKeywordsIdx，如果指定了AssKeywordsIdx，两者要同时满足。
        self.pos_keywords_idx = pos_keywords_idx
        # 舆情文章id，支持多值
        self.primary_key_idx = primary_key_idx
        # 阅读数上限
        self.reads_count_max_filter = reads_count_max_filter
        # 阅读数下限
        self.reads_count_min_filter = reads_count_min_filter
        # 相关性分上限
        self.relevance_score_max_filter = relevance_score_max_filter
        # 相关性分下限
        self.relevance_score_min_filter = relevance_score_min_filter
        # 转发数上限
        self.reposts_count_max_filter = reposts_count_max_filter
        # 转发数下限
        self.reposts_count_min_filter = reposts_count_min_filter
        # 文章转载来源名称
        self.reprint_from_filter = reprint_from_filter
        # 标题不包含的关键词
        self.title_excluding_words_idx = title_excluding_words_idx
        # 标题包含的关键词
        self.title_including_words_idx = title_including_words_idx
        # 指定索引模式,KEYWORD|CREATE_TIME
        self.used_index_mode_switch = used_index_mode_switch
        # 色情取值true or false
        self.eroticism_filter = eroticism_filter
        # 赌博取值true or false
        self.gambling_filter = gambling_filter
        # 暴恐政取值true or false
        self.bkz_filter = bkz_filter
        # 广告取值true or false
        self.advertisement_filter = advertisement_filter
        # 违规广告取值true or false
        self.illegal_advertisement_filter = illegal_advertisement_filter
        # 垃圾取值true or false
        self.spam_filter = spam_filter
        # 疑似垃圾取值true or false
        self.suspicion_spam_filter = suspicion_spam_filter
        # 业务自定义标签字段过滤
        self.biz_tags_idx = biz_tags_idx
        # 支付宝内部的2088账号
        self.alipay_account_filter = alipay_account_filter
        # 文章更新时间上限
        self.doc_update_time_end_filter = doc_update_time_end_filter
        # 更新时间戳下限
        self.doc_update_time_start_filter = doc_update_time_start_filter
        # 是否要进行关键词高亮显示
        self.enable_keyword_highlight = enable_keyword_highlight
        # 实体所在地，主要指的是公司
        self.finance_entity_area_filter = finance_entity_area_filter
        # 公司全名称
        self.entity_name = entity_name
        # 实体关联度得分上限
        self.finance_entity_relevance_score_max_filter = finance_entity_relevance_score_max_filter
        # 实体关联度得分下限
        self.finance_entity_relevance_score_min_filter = finance_entity_relevance_score_min_filter
        # 金融事件id，支持多个
        self.finance_event_code_filter = finance_event_code_filter
        # 父文章docId
        self.parent_ids_idx = parent_ids_idx
        # 如'+'是升序，'-'是降序
        self.sort_by_direction = sort_by_direction
        # 排序字段枚举
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.filter_id is not None:
            result['filterId'] = self.filter_id
        if self.ass_keywords_idx is not None:
            result['assKeywordsIdx'] = self.ass_keywords_idx
        if self.author_followers_count_max_filter is not None:
            result['authorFollowersCountMaxFilter'] = self.author_followers_count_max_filter
        if self.author_followers_count_min_filter is not None:
            result['authorFollowersCountMinFilter'] = self.author_followers_count_min_filter
        if self.author_name_idx is not None:
            result['authorNameIdx'] = self.author_name_idx
        if self.author_verify_type_filter is not None:
            result['authorVerifyTypeFilter'] = self.author_verify_type_filter
        if self.comments_count_max_filter is not None:
            result['commentsCountMaxFilter'] = self.comments_count_max_filter
        if self.comments_count_min_filter is not None:
            result['commentsCountMinFilter'] = self.comments_count_min_filter
        if self.content_length_max_filter is not None:
            result['contentLengthMaxFilter'] = self.content_length_max_filter
        if self.content_length_min_filter is not None:
            result['contentLengthMinFilter'] = self.content_length_min_filter
        if self.doc_answers_count_max_filter is not None:
            result['docAnswersCountMaxFilter'] = self.doc_answers_count_max_filter
        if self.doc_answers_count_min_filter is not None:
            result['docAnswersCountMinFilter'] = self.doc_answers_count_min_filter
        if self.doc_area_idx is not None:
            result['docAreaIdx'] = self.doc_area_idx
        if self.doc_content_sign_idx is not None:
            result['docContentSignIdx'] = self.doc_content_sign_idx
        if self.doc_create_time_end_filter is not None:
            result['docCreateTimeEndFilter'] = self.doc_create_time_end_filter
        if self.doc_create_time_start_filter is not None:
            result['docCreateTimeStartFilter'] = self.doc_create_time_start_filter
        if self.doc_publish_time_end_filter is not None:
            result['docPublishTimeEndFilter'] = self.doc_publish_time_end_filter
        if self.doc_publish_time_start_filter is not None:
            result['docPublishTimeStartFilter'] = self.doc_publish_time_start_filter
        if self.duplicate_removal is not None:
            result['duplicateRemoval'] = self.duplicate_removal
        if self.emotion_score_max_filter is not None:
            result['emotionScoreMaxFilter'] = self.emotion_score_max_filter
        if self.emotion_score_min_filter is not None:
            result['emotionScoreMinFilter'] = self.emotion_score_min_filter
        if self.exclude_author_name_idx is not None:
            result['excludeAuthorNameIdx'] = self.exclude_author_name_idx
        if self.excluding_media_hosts_filter is not None:
            result['excludingMediaHostsFilter'] = self.excluding_media_hosts_filter
        if self.excluding_media_pool_ids_filter is not None:
            result['excludingMediaPoolIdsFilter'] = self.excluding_media_pool_ids_filter
        if self.likes_count_max_filter is not None:
            result['likesCountMaxFilter'] = self.likes_count_max_filter
        if self.likes_count_min_filter is not None:
            result['likesCountMinFilter'] = self.likes_count_min_filter
        if self.media_hosts_filter is not None:
            result['mediaHostsFilter'] = self.media_hosts_filter
        if self.media_influence_score_max_filter is not None:
            result['mediaInfluenceScoreMaxFilter'] = self.media_influence_score_max_filter
        if self.media_influence_score_min_filter is not None:
            result['mediaInfluenceScoreMinFilter'] = self.media_influence_score_min_filter
        if self.media_pool_ids_filter is not None:
            result['mediaPoolIdsFilter'] = self.media_pool_ids_filter
        if self.media_propagation_score_max_filter is not None:
            result['mediaPropagationScoreMaxFilter'] = self.media_propagation_score_max_filter
        if self.media_propagation_score_min_filter is not None:
            result['mediaPropagationScoreMinFilter'] = self.media_propagation_score_min_filter
        if self.media_type_filter is not None:
            result['mediaTypeFilter'] = self.media_type_filter
        if self.message_type_filter is not None:
            result['messageTypeFilter'] = self.message_type_filter
        if self.neg_keywords_idx is not None:
            result['negKeywordsIdx'] = self.neg_keywords_idx
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.pos_keywords_idx is not None:
            result['posKeywordsIdx'] = self.pos_keywords_idx
        if self.primary_key_idx is not None:
            result['primaryKeyIdx'] = self.primary_key_idx
        if self.reads_count_max_filter is not None:
            result['readsCountMaxFilter'] = self.reads_count_max_filter
        if self.reads_count_min_filter is not None:
            result['readsCountMinFilter'] = self.reads_count_min_filter
        if self.relevance_score_max_filter is not None:
            result['relevanceScoreMaxFilter'] = self.relevance_score_max_filter
        if self.relevance_score_min_filter is not None:
            result['relevanceScoreMinFilter'] = self.relevance_score_min_filter
        if self.reposts_count_max_filter is not None:
            result['repostsCountMaxFilter'] = self.reposts_count_max_filter
        if self.reposts_count_min_filter is not None:
            result['repostsCountMinFilter'] = self.reposts_count_min_filter
        if self.reprint_from_filter is not None:
            result['reprintFromFilter'] = self.reprint_from_filter
        if self.title_excluding_words_idx is not None:
            result['titleExcludingWordsIdx'] = self.title_excluding_words_idx
        if self.title_including_words_idx is not None:
            result['titleIncludingWordsIdx'] = self.title_including_words_idx
        if self.used_index_mode_switch is not None:
            result['usedIndexModeSwitch'] = self.used_index_mode_switch
        if self.eroticism_filter is not None:
            result['eroticismFilter'] = self.eroticism_filter
        if self.gambling_filter is not None:
            result['gamblingFilter'] = self.gambling_filter
        if self.bkz_filter is not None:
            result['bkzFilter'] = self.bkz_filter
        if self.advertisement_filter is not None:
            result['advertisementFilter'] = self.advertisement_filter
        if self.illegal_advertisement_filter is not None:
            result['illegalAdvertisementFilter'] = self.illegal_advertisement_filter
        if self.spam_filter is not None:
            result['spamFilter'] = self.spam_filter
        if self.suspicion_spam_filter is not None:
            result['suspicionSpamFilter'] = self.suspicion_spam_filter
        if self.biz_tags_idx is not None:
            result['bizTagsIdx'] = self.biz_tags_idx
        if self.alipay_account_filter is not None:
            result['alipayAccountFilter'] = self.alipay_account_filter
        if self.doc_update_time_end_filter is not None:
            result['docUpdateTimeEndFilter'] = self.doc_update_time_end_filter
        if self.doc_update_time_start_filter is not None:
            result['docUpdateTimeStartFilter'] = self.doc_update_time_start_filter
        if self.enable_keyword_highlight is not None:
            result['enableKeywordHighlight'] = self.enable_keyword_highlight
        if self.finance_entity_area_filter is not None:
            result['financeEntityAreaFilter'] = self.finance_entity_area_filter
        if self.entity_name is not None:
            result['entityName'] = self.entity_name
        if self.finance_entity_relevance_score_max_filter is not None:
            result['financeEntityRelevanceScoreMaxFilter'] = self.finance_entity_relevance_score_max_filter
        if self.finance_entity_relevance_score_min_filter is not None:
            result['financeEntityRelevanceScoreMinFilter'] = self.finance_entity_relevance_score_min_filter
        if self.finance_event_code_filter is not None:
            result['financeEventCodeFilter'] = self.finance_event_code_filter
        if self.parent_ids_idx is not None:
            result['parentIdsIdx'] = self.parent_ids_idx
        if self.sort_by_direction is not None:
            result['sortByDirection'] = self.sort_by_direction
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('filterId') is not None:
            self.filter_id = m.get('filterId')
        if m.get('assKeywordsIdx') is not None:
            self.ass_keywords_idx = m.get('assKeywordsIdx')
        if m.get('authorFollowersCountMaxFilter') is not None:
            self.author_followers_count_max_filter = m.get('authorFollowersCountMaxFilter')
        if m.get('authorFollowersCountMinFilter') is not None:
            self.author_followers_count_min_filter = m.get('authorFollowersCountMinFilter')
        if m.get('authorNameIdx') is not None:
            self.author_name_idx = m.get('authorNameIdx')
        if m.get('authorVerifyTypeFilter') is not None:
            self.author_verify_type_filter = m.get('authorVerifyTypeFilter')
        if m.get('commentsCountMaxFilter') is not None:
            self.comments_count_max_filter = m.get('commentsCountMaxFilter')
        if m.get('commentsCountMinFilter') is not None:
            self.comments_count_min_filter = m.get('commentsCountMinFilter')
        if m.get('contentLengthMaxFilter') is not None:
            self.content_length_max_filter = m.get('contentLengthMaxFilter')
        if m.get('contentLengthMinFilter') is not None:
            self.content_length_min_filter = m.get('contentLengthMinFilter')
        if m.get('docAnswersCountMaxFilter') is not None:
            self.doc_answers_count_max_filter = m.get('docAnswersCountMaxFilter')
        if m.get('docAnswersCountMinFilter') is not None:
            self.doc_answers_count_min_filter = m.get('docAnswersCountMinFilter')
        if m.get('docAreaIdx') is not None:
            self.doc_area_idx = m.get('docAreaIdx')
        if m.get('docContentSignIdx') is not None:
            self.doc_content_sign_idx = m.get('docContentSignIdx')
        if m.get('docCreateTimeEndFilter') is not None:
            self.doc_create_time_end_filter = m.get('docCreateTimeEndFilter')
        if m.get('docCreateTimeStartFilter') is not None:
            self.doc_create_time_start_filter = m.get('docCreateTimeStartFilter')
        if m.get('docPublishTimeEndFilter') is not None:
            self.doc_publish_time_end_filter = m.get('docPublishTimeEndFilter')
        if m.get('docPublishTimeStartFilter') is not None:
            self.doc_publish_time_start_filter = m.get('docPublishTimeStartFilter')
        if m.get('duplicateRemoval') is not None:
            self.duplicate_removal = m.get('duplicateRemoval')
        if m.get('emotionScoreMaxFilter') is not None:
            self.emotion_score_max_filter = m.get('emotionScoreMaxFilter')
        if m.get('emotionScoreMinFilter') is not None:
            self.emotion_score_min_filter = m.get('emotionScoreMinFilter')
        if m.get('excludeAuthorNameIdx') is not None:
            self.exclude_author_name_idx = m.get('excludeAuthorNameIdx')
        if m.get('excludingMediaHostsFilter') is not None:
            self.excluding_media_hosts_filter = m.get('excludingMediaHostsFilter')
        if m.get('excludingMediaPoolIdsFilter') is not None:
            self.excluding_media_pool_ids_filter = m.get('excludingMediaPoolIdsFilter')
        if m.get('likesCountMaxFilter') is not None:
            self.likes_count_max_filter = m.get('likesCountMaxFilter')
        if m.get('likesCountMinFilter') is not None:
            self.likes_count_min_filter = m.get('likesCountMinFilter')
        if m.get('mediaHostsFilter') is not None:
            self.media_hosts_filter = m.get('mediaHostsFilter')
        if m.get('mediaInfluenceScoreMaxFilter') is not None:
            self.media_influence_score_max_filter = m.get('mediaInfluenceScoreMaxFilter')
        if m.get('mediaInfluenceScoreMinFilter') is not None:
            self.media_influence_score_min_filter = m.get('mediaInfluenceScoreMinFilter')
        if m.get('mediaPoolIdsFilter') is not None:
            self.media_pool_ids_filter = m.get('mediaPoolIdsFilter')
        if m.get('mediaPropagationScoreMaxFilter') is not None:
            self.media_propagation_score_max_filter = m.get('mediaPropagationScoreMaxFilter')
        if m.get('mediaPropagationScoreMinFilter') is not None:
            self.media_propagation_score_min_filter = m.get('mediaPropagationScoreMinFilter')
        if m.get('mediaTypeFilter') is not None:
            self.media_type_filter = m.get('mediaTypeFilter')
        if m.get('messageTypeFilter') is not None:
            self.message_type_filter = m.get('messageTypeFilter')
        if m.get('negKeywordsIdx') is not None:
            self.neg_keywords_idx = m.get('negKeywordsIdx')
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('posKeywordsIdx') is not None:
            self.pos_keywords_idx = m.get('posKeywordsIdx')
        if m.get('primaryKeyIdx') is not None:
            self.primary_key_idx = m.get('primaryKeyIdx')
        if m.get('readsCountMaxFilter') is not None:
            self.reads_count_max_filter = m.get('readsCountMaxFilter')
        if m.get('readsCountMinFilter') is not None:
            self.reads_count_min_filter = m.get('readsCountMinFilter')
        if m.get('relevanceScoreMaxFilter') is not None:
            self.relevance_score_max_filter = m.get('relevanceScoreMaxFilter')
        if m.get('relevanceScoreMinFilter') is not None:
            self.relevance_score_min_filter = m.get('relevanceScoreMinFilter')
        if m.get('repostsCountMaxFilter') is not None:
            self.reposts_count_max_filter = m.get('repostsCountMaxFilter')
        if m.get('repostsCountMinFilter') is not None:
            self.reposts_count_min_filter = m.get('repostsCountMinFilter')
        if m.get('reprintFromFilter') is not None:
            self.reprint_from_filter = m.get('reprintFromFilter')
        if m.get('titleExcludingWordsIdx') is not None:
            self.title_excluding_words_idx = m.get('titleExcludingWordsIdx')
        if m.get('titleIncludingWordsIdx') is not None:
            self.title_including_words_idx = m.get('titleIncludingWordsIdx')
        if m.get('usedIndexModeSwitch') is not None:
            self.used_index_mode_switch = m.get('usedIndexModeSwitch')
        if m.get('eroticismFilter') is not None:
            self.eroticism_filter = m.get('eroticismFilter')
        if m.get('gamblingFilter') is not None:
            self.gambling_filter = m.get('gamblingFilter')
        if m.get('bkzFilter') is not None:
            self.bkz_filter = m.get('bkzFilter')
        if m.get('advertisementFilter') is not None:
            self.advertisement_filter = m.get('advertisementFilter')
        if m.get('illegalAdvertisementFilter') is not None:
            self.illegal_advertisement_filter = m.get('illegalAdvertisementFilter')
        if m.get('spamFilter') is not None:
            self.spam_filter = m.get('spamFilter')
        if m.get('suspicionSpamFilter') is not None:
            self.suspicion_spam_filter = m.get('suspicionSpamFilter')
        if m.get('bizTagsIdx') is not None:
            self.biz_tags_idx = m.get('bizTagsIdx')
        if m.get('alipayAccountFilter') is not None:
            self.alipay_account_filter = m.get('alipayAccountFilter')
        if m.get('docUpdateTimeEndFilter') is not None:
            self.doc_update_time_end_filter = m.get('docUpdateTimeEndFilter')
        if m.get('docUpdateTimeStartFilter') is not None:
            self.doc_update_time_start_filter = m.get('docUpdateTimeStartFilter')
        if m.get('enableKeywordHighlight') is not None:
            self.enable_keyword_highlight = m.get('enableKeywordHighlight')
        if m.get('financeEntityAreaFilter') is not None:
            self.finance_entity_area_filter = m.get('financeEntityAreaFilter')
        if m.get('entityName') is not None:
            self.entity_name = m.get('entityName')
        if m.get('financeEntityRelevanceScoreMaxFilter') is not None:
            self.finance_entity_relevance_score_max_filter = m.get('financeEntityRelevanceScoreMaxFilter')
        if m.get('financeEntityRelevanceScoreMinFilter') is not None:
            self.finance_entity_relevance_score_min_filter = m.get('financeEntityRelevanceScoreMinFilter')
        if m.get('financeEventCodeFilter') is not None:
            self.finance_event_code_filter = m.get('financeEventCodeFilter')
        if m.get('parentIdsIdx') is not None:
            self.parent_ids_idx = m.get('parentIdsIdx')
        if m.get('sortByDirection') is not None:
            self.sort_by_direction = m.get('sortByDirection')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        return self


class FinanceEvent(TeaModel):
    def __init__(
        self,
        entity_area: str = None,
        entity_id: str = None,
        entity_name: str = None,
        entity_relevance_score: str = None,
        entity_summary: str = None,
        entity_type: str = None,
        event_code: int = None,
        event_id: str = None,
        event_name: str = None,
        entity_crn: str = None,
    ):
        # 实体地理位置
        self.entity_area = entity_area
        # 实体ID
        self.entity_id = entity_id
        # 实体名称
        self.entity_name = entity_name
        # 实体相关度得分
        self.entity_relevance_score = entity_relevance_score
        # 实体的事件摘要描述
        self.entity_summary = entity_summary
        # 实体类型，枚举值
        self.entity_type = entity_type
        # 事件码
        self.event_code = event_code
        # 事件id
        self.event_id = event_id
        # 事件名称
        self.event_name = event_name
        # 实体唯一id，统一社会信用代码
        self.entity_crn = entity_crn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.entity_area is not None:
            result['entityArea'] = self.entity_area
        if self.entity_id is not None:
            result['entityId'] = self.entity_id
        if self.entity_name is not None:
            result['entityName'] = self.entity_name
        if self.entity_relevance_score is not None:
            result['entityRelevanceScore'] = self.entity_relevance_score
        if self.entity_summary is not None:
            result['entitySummary'] = self.entity_summary
        if self.entity_type is not None:
            result['entityType'] = self.entity_type
        if self.event_code is not None:
            result['eventCode'] = self.event_code
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.event_name is not None:
            result['eventName'] = self.event_name
        if self.entity_crn is not None:
            result['entityCrn'] = self.entity_crn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityArea') is not None:
            self.entity_area = m.get('entityArea')
        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')
        if m.get('entityName') is not None:
            self.entity_name = m.get('entityName')
        if m.get('entityRelevanceScore') is not None:
            self.entity_relevance_score = m.get('entityRelevanceScore')
        if m.get('entitySummary') is not None:
            self.entity_summary = m.get('entitySummary')
        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')
        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')
        if m.get('entityCrn') is not None:
            self.entity_crn = m.get('entityCrn')
        return self


class Filter(TeaModel):
    def __init__(
        self,
        id: int = None,
        gmt_create_timestamp: int = None,
        gmt_modified_timestamp: int = None,
        valid: int = None,
        name: str = None,
        criteria: str = None,
        filter_group_id: int = None,
    ):
        # 筛选模板id
        self.id = id
        # 创建日期，毫秒
        self.gmt_create_timestamp = gmt_create_timestamp
        # 修改时间，毫秒
        self.gmt_modified_timestamp = gmt_modified_timestamp
        # 状态。1：有效，0：无效
        self.valid = valid
        # 筛选模板名称
        self.name = name
        # 筛选模板配置内容
        self.criteria = criteria
        # 筛选模板所属id
        self.filter_group_id = filter_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.gmt_create_timestamp is not None:
            result['gmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.valid is not None:
            result['valid'] = self.valid
        if self.name is not None:
            result['name'] = self.name
        if self.criteria is not None:
            result['criteria'] = self.criteria
        if self.filter_group_id is not None:
            result['filterGroupId'] = self.filter_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('gmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('gmtCreateTimestamp')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('criteria') is not None:
            self.criteria = m.get('criteria')
        if m.get('filterGroupId') is not None:
            self.filter_group_id = m.get('filterGroupId')
        return self


class StatisticPoint(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: float = None,
    ):
        # 聚合字段结果值
        self.key = key
        # 聚合结果值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class YuqingMessage(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        advertisement: bool = None,
        alipay_account: int = None,
        at_author_names: List[str] = None,
        author_avatar_url: str = None,
        author_followers_count: int = None,
        author_friends_count: int = None,
        author_id: str = None,
        author_name: str = None,
        author_profile_url: str = None,
        author_statuses_count: int = None,
        author_verify_type: str = None,
        bkz: bool = None,
        content_audio_text: str = None,
        content_audio_urls: str = None,
        content_emotion_type: int = None,
        content_image_text: str = None,
        content_image_urls: str = None,
        content_video_text: str = None,
        content_video_urls: str = None,
        doc_create_time: int = None,
        doc_publish_time: int = None,
        doc_answers_count: int = None,
        doc_areas: List[str] = None,
        doc_comments_count: int = None,
        doc_content: str = None,
        doc_content_brief: str = None,
        doc_content_sign: str = None,
        doc_focus_article_count: int = None,
        doc_likes_count: int = None,
        doc_message_type: str = None,
        doc_parent_id: str = None,
        doc_reads_count: int = None,
        doc_reposts_count: int = None,
        doc_self_content_sign: str = None,
        doc_title: str = None,
        doc_title_brief: str = None,
        doc_url: str = None,
        doc_user_define_json: str = None,
        emotion_score: str = None,
        entity_alias: str = None,
        entity_relevancy_score: str = None,
        eroticism: bool = None,
        eroticism_score_fmt: str = None,
        gambling: bool = None,
        highlight_ass_keywords: List[str] = None,
        highlight_keywords: List[str] = None,
        highlight_pos_keywords: List[str] = None,
        image_count: int = None,
        media_hosts: List[str] = None,
        media_influence_level: int = None,
        media_influence_score: str = None,
        media_name: str = None,
        media_propagation_score: str = None,
        media_qun_name: str = None,
        media_res_city: str = None,
        media_res_country: str = None,
        media_res_province: str = None,
        media_type: str = None,
        original_media: List[str] = None,
        relevance_score_fmt: str = None,
        similar_number: int = None,
        spam: bool = None,
        weibo_comment_id: str = None,
        weibo_mid: str = None,
        ue_emotion_score: str = None,
        finance_events: List[FinanceEvent] = None,
    ):
        # 舆情文章唯一ID
        self.doc_id = doc_id
        # 广告
        self.advertisement = advertisement
        # 2088账号
        self.alipay_account = alipay_account
        # 被at的用户名列表
        self.at_author_names = at_author_names
        # 用户头像地址
        self.author_avatar_url = author_avatar_url
        # 作者粉丝数
        self.author_followers_count = author_followers_count
        # 作者好友数
        self.author_friends_count = author_friends_count
        # 外部平台作者id
        self.author_id = author_id
        # 作者名称
        self.author_name = author_name
        # 个人主页地址
        self.author_profile_url = author_profile_url
        # 发布微博数
        self.author_statuses_count = author_statuses_count
        # 作者认证类型
        self.author_verify_type = author_verify_type
        # 敏感暴恐政
        self.bkz = bkz
        # 音频识别出来的文字
        self.content_audio_text = content_audio_text
        # 音频地址
        self.content_audio_urls = content_audio_urls
        # 情感的正负面，-1代表负面，1代表非负面
        self.content_emotion_type = content_emotion_type
        # 从图片识别出来文字
        self.content_image_text = content_image_text
        # 内容中的图片列表
        self.content_image_urls = content_image_urls
        # 视频识别出来的文字
        self.content_video_text = content_video_text
        # 视频地址
        self.content_video_urls = content_video_urls
        # 舆情文章入库时间戳
        self.doc_create_time = doc_create_time
        # 舆情文章的发布时间戳
        self.doc_publish_time = doc_publish_time
        # 回答数
        self.doc_answers_count = doc_answers_count
        # 新闻用内容提取的地名,微博用用户的地名,映射归一化
        self.doc_areas = doc_areas
        # 文章评论数
        self.doc_comments_count = doc_comments_count
        # 舆情消息内容
        self.doc_content = doc_content
        # 文章内容概要，无Html标签，最长保留200个字
        self.doc_content_brief = doc_content_brief
        # 文章内容签名，如果是转发微博或者其他有父内容的doc，计算的是父文章的得分。一般用于去重，相同的doc_content_sign说明内容相同
        self.doc_content_sign = doc_content_sign
        # 文章的关注数
        self.doc_focus_article_count = doc_focus_article_count
        # 文章点赞数
        self.doc_likes_count = doc_likes_count
        # 舆情消息类型:转发,评论/回复, 原文,群聊等
        self.doc_message_type = doc_message_type
        # 父文章DocID, 比如转发微博的父Id是源微博DocId
        self.doc_parent_id = doc_parent_id
        # 阅读数
        self.doc_reads_count = doc_reads_count
        # 转载数
        self.doc_reposts_count = doc_reposts_count
        # 文章自身的内容签名，转发微博计算的是转发内容的contentSign，与父微博无关
        self.doc_self_content_sign = doc_self_content_sign
        # 文章的标题
        self.doc_title = doc_title
        # 文章标题，无Html标签
        self.doc_title_brief = doc_title_brief
        # 原文链接
        self.doc_url = doc_url
        # 业务自定义字段透传docUserDefineJson
        self.doc_user_define_json = doc_user_define_json
        # 情感得分
        self.emotion_score = emotion_score
        # 实体别名
        self.entity_alias = entity_alias
        # 实体相关度得分，0-1,两位小数
        self.entity_relevancy_score = entity_relevancy_score
        # 是否色情内容
        self.eroticism = eroticism
        # 内容的暴恐政色得分，0-10，值越大说明内容越敏感
        self.eroticism_score_fmt = eroticism_score_fmt
        # 是否涉及赌博
        self.gambling = gambling
        # 如果查询条件中有搭配词，那么这个字段存储文章中命中的搭配词列表
        self.highlight_ass_keywords = highlight_ass_keywords
        # 在指定关键词、搭配词的情况下，返回文章内命中的词列表
        self.highlight_keywords = highlight_keywords
        # 如果查询条件中有关键词，那么这个字段保存文章中命中的关键词列表
        self.highlight_pos_keywords = highlight_pos_keywords
        # 文章内容中的图片个数
        self.image_count = image_count
        # 站点来源host列表
        self.media_hosts = media_hosts
        # 媒体影响力等级，0-4，值越大影响力越大
        self.media_influence_level = media_influence_level
        # 媒体影响力 0-10,两位小数
        self.media_influence_score = media_influence_score
        # 媒体名称
        self.media_name = media_name
        # 媒体传播得分，0-10,两位小数
        self.media_propagation_score = media_propagation_score
        # IM软件群聊天名称
        self.media_qun_name = media_qun_name
        # 媒体地域信息: 城市
        self.media_res_city = media_res_city
        # 媒体地域信息: 国家
        self.media_res_country = media_res_country
        # 媒体地域信息: 省份
        self.media_res_province = media_res_province
        # 媒体类型，枚举值
        self.media_type = media_type
        # 疑似首发媒体列表
        self.original_media = original_media
        # 关键词/搭配词与文章内容的相关性得分，0-10分，值越大相关性越高
        self.relevance_score_fmt = relevance_score_fmt
        # 相似文章数
        self.similar_number = similar_number
        # 是否垃圾内容
        self.spam = spam
        # 微博评论的外部ID
        self.weibo_comment_id = weibo_comment_id
        # 微博外部ID
        self.weibo_mid = weibo_mid
        # 用户情感分值
        self.ue_emotion_score = ue_emotion_score
        # 舆情文章提取出来的金融事件列表
        self.finance_events = finance_events

    def validate(self):
        if self.finance_events:
            for k in self.finance_events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.advertisement is not None:
            result['advertisement'] = self.advertisement
        if self.alipay_account is not None:
            result['alipayAccount'] = self.alipay_account
        if self.at_author_names is not None:
            result['atAuthorNames'] = self.at_author_names
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
        if self.author_profile_url is not None:
            result['authorProfileUrl'] = self.author_profile_url
        if self.author_statuses_count is not None:
            result['authorStatusesCount'] = self.author_statuses_count
        if self.author_verify_type is not None:
            result['authorVerifyType'] = self.author_verify_type
        if self.bkz is not None:
            result['bkz'] = self.bkz
        if self.content_audio_text is not None:
            result['contentAudioText'] = self.content_audio_text
        if self.content_audio_urls is not None:
            result['contentAudioUrls'] = self.content_audio_urls
        if self.content_emotion_type is not None:
            result['contentEmotionType'] = self.content_emotion_type
        if self.content_image_text is not None:
            result['contentImageText'] = self.content_image_text
        if self.content_image_urls is not None:
            result['contentImageUrls'] = self.content_image_urls
        if self.content_video_text is not None:
            result['contentVideoText'] = self.content_video_text
        if self.content_video_urls is not None:
            result['contentVideoUrls'] = self.content_video_urls
        if self.doc_create_time is not None:
            result['docCreateTime'] = self.doc_create_time
        if self.doc_publish_time is not None:
            result['docPublishTime'] = self.doc_publish_time
        if self.doc_answers_count is not None:
            result['docAnswersCount'] = self.doc_answers_count
        if self.doc_areas is not None:
            result['docAreas'] = self.doc_areas
        if self.doc_comments_count is not None:
            result['docCommentsCount'] = self.doc_comments_count
        if self.doc_content is not None:
            result['docContent'] = self.doc_content
        if self.doc_content_brief is not None:
            result['docContentBrief'] = self.doc_content_brief
        if self.doc_content_sign is not None:
            result['docContentSign'] = self.doc_content_sign
        if self.doc_focus_article_count is not None:
            result['docFocusArticleCount'] = self.doc_focus_article_count
        if self.doc_likes_count is not None:
            result['docLikesCount'] = self.doc_likes_count
        if self.doc_message_type is not None:
            result['docMessageType'] = self.doc_message_type
        if self.doc_parent_id is not None:
            result['docParentId'] = self.doc_parent_id
        if self.doc_reads_count is not None:
            result['docReadsCount'] = self.doc_reads_count
        if self.doc_reposts_count is not None:
            result['docRepostsCount'] = self.doc_reposts_count
        if self.doc_self_content_sign is not None:
            result['docSelfContentSign'] = self.doc_self_content_sign
        if self.doc_title is not None:
            result['docTitle'] = self.doc_title
        if self.doc_title_brief is not None:
            result['docTitleBrief'] = self.doc_title_brief
        if self.doc_url is not None:
            result['docUrl'] = self.doc_url
        if self.doc_user_define_json is not None:
            result['docUserDefineJson'] = self.doc_user_define_json
        if self.emotion_score is not None:
            result['emotionScore'] = self.emotion_score
        if self.entity_alias is not None:
            result['entityAlias'] = self.entity_alias
        if self.entity_relevancy_score is not None:
            result['entityRelevancyScore'] = self.entity_relevancy_score
        if self.eroticism is not None:
            result['eroticism'] = self.eroticism
        if self.eroticism_score_fmt is not None:
            result['eroticismScoreFmt'] = self.eroticism_score_fmt
        if self.gambling is not None:
            result['gambling'] = self.gambling
        if self.highlight_ass_keywords is not None:
            result['highlightAssKeywords'] = self.highlight_ass_keywords
        if self.highlight_keywords is not None:
            result['highlightKeywords'] = self.highlight_keywords
        if self.highlight_pos_keywords is not None:
            result['highlightPosKeywords'] = self.highlight_pos_keywords
        if self.image_count is not None:
            result['imageCount'] = self.image_count
        if self.media_hosts is not None:
            result['mediaHosts'] = self.media_hosts
        if self.media_influence_level is not None:
            result['mediaInfluenceLevel'] = self.media_influence_level
        if self.media_influence_score is not None:
            result['mediaInfluenceScore'] = self.media_influence_score
        if self.media_name is not None:
            result['mediaName'] = self.media_name
        if self.media_propagation_score is not None:
            result['mediaPropagationScore'] = self.media_propagation_score
        if self.media_qun_name is not None:
            result['mediaQunName'] = self.media_qun_name
        if self.media_res_city is not None:
            result['mediaResCity'] = self.media_res_city
        if self.media_res_country is not None:
            result['mediaResCountry'] = self.media_res_country
        if self.media_res_province is not None:
            result['mediaResProvince'] = self.media_res_province
        if self.media_type is not None:
            result['mediaType'] = self.media_type
        if self.original_media is not None:
            result['originalMedia'] = self.original_media
        if self.relevance_score_fmt is not None:
            result['relevanceScoreFmt'] = self.relevance_score_fmt
        if self.similar_number is not None:
            result['similarNumber'] = self.similar_number
        if self.spam is not None:
            result['spam'] = self.spam
        if self.weibo_comment_id is not None:
            result['weiboCommentId'] = self.weibo_comment_id
        if self.weibo_mid is not None:
            result['weiboMid'] = self.weibo_mid
        if self.ue_emotion_score is not None:
            result['ueEmotionScore'] = self.ue_emotion_score
        result['financeEvents'] = []
        if self.finance_events is not None:
            for k in self.finance_events:
                result['financeEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('advertisement') is not None:
            self.advertisement = m.get('advertisement')
        if m.get('alipayAccount') is not None:
            self.alipay_account = m.get('alipayAccount')
        if m.get('atAuthorNames') is not None:
            self.at_author_names = m.get('atAuthorNames')
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
        if m.get('authorProfileUrl') is not None:
            self.author_profile_url = m.get('authorProfileUrl')
        if m.get('authorStatusesCount') is not None:
            self.author_statuses_count = m.get('authorStatusesCount')
        if m.get('authorVerifyType') is not None:
            self.author_verify_type = m.get('authorVerifyType')
        if m.get('bkz') is not None:
            self.bkz = m.get('bkz')
        if m.get('contentAudioText') is not None:
            self.content_audio_text = m.get('contentAudioText')
        if m.get('contentAudioUrls') is not None:
            self.content_audio_urls = m.get('contentAudioUrls')
        if m.get('contentEmotionType') is not None:
            self.content_emotion_type = m.get('contentEmotionType')
        if m.get('contentImageText') is not None:
            self.content_image_text = m.get('contentImageText')
        if m.get('contentImageUrls') is not None:
            self.content_image_urls = m.get('contentImageUrls')
        if m.get('contentVideoText') is not None:
            self.content_video_text = m.get('contentVideoText')
        if m.get('contentVideoUrls') is not None:
            self.content_video_urls = m.get('contentVideoUrls')
        if m.get('docCreateTime') is not None:
            self.doc_create_time = m.get('docCreateTime')
        if m.get('docPublishTime') is not None:
            self.doc_publish_time = m.get('docPublishTime')
        if m.get('docAnswersCount') is not None:
            self.doc_answers_count = m.get('docAnswersCount')
        if m.get('docAreas') is not None:
            self.doc_areas = m.get('docAreas')
        if m.get('docCommentsCount') is not None:
            self.doc_comments_count = m.get('docCommentsCount')
        if m.get('docContent') is not None:
            self.doc_content = m.get('docContent')
        if m.get('docContentBrief') is not None:
            self.doc_content_brief = m.get('docContentBrief')
        if m.get('docContentSign') is not None:
            self.doc_content_sign = m.get('docContentSign')
        if m.get('docFocusArticleCount') is not None:
            self.doc_focus_article_count = m.get('docFocusArticleCount')
        if m.get('docLikesCount') is not None:
            self.doc_likes_count = m.get('docLikesCount')
        if m.get('docMessageType') is not None:
            self.doc_message_type = m.get('docMessageType')
        if m.get('docParentId') is not None:
            self.doc_parent_id = m.get('docParentId')
        if m.get('docReadsCount') is not None:
            self.doc_reads_count = m.get('docReadsCount')
        if m.get('docRepostsCount') is not None:
            self.doc_reposts_count = m.get('docRepostsCount')
        if m.get('docSelfContentSign') is not None:
            self.doc_self_content_sign = m.get('docSelfContentSign')
        if m.get('docTitle') is not None:
            self.doc_title = m.get('docTitle')
        if m.get('docTitleBrief') is not None:
            self.doc_title_brief = m.get('docTitleBrief')
        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')
        if m.get('docUserDefineJson') is not None:
            self.doc_user_define_json = m.get('docUserDefineJson')
        if m.get('emotionScore') is not None:
            self.emotion_score = m.get('emotionScore')
        if m.get('entityAlias') is not None:
            self.entity_alias = m.get('entityAlias')
        if m.get('entityRelevancyScore') is not None:
            self.entity_relevancy_score = m.get('entityRelevancyScore')
        if m.get('eroticism') is not None:
            self.eroticism = m.get('eroticism')
        if m.get('eroticismScoreFmt') is not None:
            self.eroticism_score_fmt = m.get('eroticismScoreFmt')
        if m.get('gambling') is not None:
            self.gambling = m.get('gambling')
        if m.get('highlightAssKeywords') is not None:
            self.highlight_ass_keywords = m.get('highlightAssKeywords')
        if m.get('highlightKeywords') is not None:
            self.highlight_keywords = m.get('highlightKeywords')
        if m.get('highlightPosKeywords') is not None:
            self.highlight_pos_keywords = m.get('highlightPosKeywords')
        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')
        if m.get('mediaHosts') is not None:
            self.media_hosts = m.get('mediaHosts')
        if m.get('mediaInfluenceLevel') is not None:
            self.media_influence_level = m.get('mediaInfluenceLevel')
        if m.get('mediaInfluenceScore') is not None:
            self.media_influence_score = m.get('mediaInfluenceScore')
        if m.get('mediaName') is not None:
            self.media_name = m.get('mediaName')
        if m.get('mediaPropagationScore') is not None:
            self.media_propagation_score = m.get('mediaPropagationScore')
        if m.get('mediaQunName') is not None:
            self.media_qun_name = m.get('mediaQunName')
        if m.get('mediaResCity') is not None:
            self.media_res_city = m.get('mediaResCity')
        if m.get('mediaResCountry') is not None:
            self.media_res_country = m.get('mediaResCountry')
        if m.get('mediaResProvince') is not None:
            self.media_res_province = m.get('mediaResProvince')
        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')
        if m.get('originalMedia') is not None:
            self.original_media = m.get('originalMedia')
        if m.get('relevanceScoreFmt') is not None:
            self.relevance_score_fmt = m.get('relevanceScoreFmt')
        if m.get('similarNumber') is not None:
            self.similar_number = m.get('similarNumber')
        if m.get('spam') is not None:
            self.spam = m.get('spam')
        if m.get('weiboCommentId') is not None:
            self.weibo_comment_id = m.get('weiboCommentId')
        if m.get('weiboMid') is not None:
            self.weibo_mid = m.get('weiboMid')
        if m.get('ueEmotionScore') is not None:
            self.ue_emotion_score = m.get('ueEmotionScore')
        self.finance_events = []
        if m.get('financeEvents') is not None:
            for k in m.get('financeEvents'):
                temp_model = FinanceEvent()
                self.finance_events.append(temp_model.from_map(k))
        return self


class ProjectGroup(TeaModel):
    def __init__(
        self,
        gmt_create_timestamp: int = None,
        gmt_modified_timestamp: int = None,
        id: int = None,
        name: str = None,
        parent_id: int = None,
        project_group_type: int = None,
        uid_create: str = None,
        uname_create: str = None,
        valid: int = None,
    ):
        # 项目分组创建时间
        self.gmt_create_timestamp = gmt_create_timestamp
        # 项目分组修改时间
        self.gmt_modified_timestamp = gmt_modified_timestamp
        # 项目分组id，唯一标识项目分组
        self.id = id
        # 项目分组名称
        self.name = name
        # 父项目分组id，0为默认值，表示无父项目分组
        self.parent_id = parent_id
        # 项目分组类型，0表示通用舆情，2表示金融舆情
        self.project_group_type = project_group_type
        # 项目创建人uid
        self.uid_create = uid_create
        # 项目分组创建人名称
        self.uname_create = uname_create
        # 是否有效，1表示有效，0表示无效
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.gmt_create_timestamp is not None:
            result['gmtCreateTimestamp'] = self.gmt_create_timestamp
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.project_group_type is not None:
            result['projectGroupType'] = self.project_group_type
        if self.uid_create is not None:
            result['uidCreate'] = self.uid_create
        if self.uname_create is not None:
            result['unameCreate'] = self.uname_create
        if self.valid is not None:
            result['valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmtCreateTimestamp') is not None:
            self.gmt_create_timestamp = m.get('gmtCreateTimestamp')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('projectGroupType') is not None:
            self.project_group_type = m.get('projectGroupType')
        if m.get('uidCreate') is not None:
            self.uid_create = m.get('uidCreate')
        if m.get('unameCreate') is not None:
            self.uname_create = m.get('unameCreate')
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        return self


class AlarmData(TeaModel):
    def __init__(
        self,
        alarm_level: str = None,
        alarm_msg_id: int = None,
        alarm_rule_id: int = None,
        alarm_rule_name: str = None,
        alarm_timestamp: int = None,
        author_name: str = None,
        content: str = None,
        doc_id_str: str = None,
        doc_media_type: str = None,
        gmt_modified_timestamp: int = None,
        media_name: str = None,
        memos: List[str] = None,
        modifier_name: str = None,
        modifier_out_no: str = None,
        project_id: int = None,
        project_name: str = None,
        self_content_sign_str: str = None,
        source_url: str = None,
        state: str = None,
        tags: List[str] = None,
        title: str = None,
        type: str = None,
        message: YuqingMessage = None,
    ):
        # 预警规则等级
        self.alarm_level = alarm_level
        # 舆情消息id
        self.alarm_msg_id = alarm_msg_id
        # 预警规则id
        self.alarm_rule_id = alarm_rule_id
        # 预警规则名称
        self.alarm_rule_name = alarm_rule_name
        # 预警时间
        self.alarm_timestamp = alarm_timestamp
        # 舆情作者名字
        self.author_name = author_name
        # 舆情内容（不完整）
        self.content = content
        # 舆情文章唯一id
        self.doc_id_str = doc_id_str
        # 舆情消息类型
        self.doc_media_type = doc_media_type
        # 最后更新时间
        self.gmt_modified_timestamp = gmt_modified_timestamp
        # 媒体名字
        self.media_name = media_name
        # 备注列表
        self.memos = memos
        # 最后修改舆情的用户名称
        self.modifier_name = modifier_name
        # 员工工号
        self.modifier_out_no = modifier_out_no
        # 项目id
        self.project_id = project_id
        # 舆情命中的预警项目名称
        self.project_name = project_name
        # 文章签名
        self.self_content_sign_str = self_content_sign_str
        # url地址
        self.source_url = source_url
        # 预警消息状态
        self.state = state
        # 预警的标签列表
        self.tags = tags
        # 舆情标题
        self.title = title
        # 预警规则类型，枚举值
        self.type = type
        # 舆情消息体
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        result = dict()
        if self.alarm_level is not None:
            result['alarmLevel'] = self.alarm_level
        if self.alarm_msg_id is not None:
            result['alarmMsgId'] = self.alarm_msg_id
        if self.alarm_rule_id is not None:
            result['alarmRuleId'] = self.alarm_rule_id
        if self.alarm_rule_name is not None:
            result['alarmRuleName'] = self.alarm_rule_name
        if self.alarm_timestamp is not None:
            result['alarmTimestamp'] = self.alarm_timestamp
        if self.author_name is not None:
            result['authorName'] = self.author_name
        if self.content is not None:
            result['content'] = self.content
        if self.doc_id_str is not None:
            result['docIdStr'] = self.doc_id_str
        if self.doc_media_type is not None:
            result['docMediaType'] = self.doc_media_type
        if self.gmt_modified_timestamp is not None:
            result['gmtModifiedTimestamp'] = self.gmt_modified_timestamp
        if self.media_name is not None:
            result['mediaName'] = self.media_name
        if self.memos is not None:
            result['memos'] = self.memos
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.modifier_out_no is not None:
            result['modifierOutNo'] = self.modifier_out_no
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.self_content_sign_str is not None:
            result['selfContentSignStr'] = self.self_content_sign_str
        if self.source_url is not None:
            result['sourceUrl'] = self.source_url
        if self.state is not None:
            result['state'] = self.state
        if self.tags is not None:
            result['tags'] = self.tags
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmLevel') is not None:
            self.alarm_level = m.get('alarmLevel')
        if m.get('alarmMsgId') is not None:
            self.alarm_msg_id = m.get('alarmMsgId')
        if m.get('alarmRuleId') is not None:
            self.alarm_rule_id = m.get('alarmRuleId')
        if m.get('alarmRuleName') is not None:
            self.alarm_rule_name = m.get('alarmRuleName')
        if m.get('alarmTimestamp') is not None:
            self.alarm_timestamp = m.get('alarmTimestamp')
        if m.get('authorName') is not None:
            self.author_name = m.get('authorName')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('docIdStr') is not None:
            self.doc_id_str = m.get('docIdStr')
        if m.get('docMediaType') is not None:
            self.doc_media_type = m.get('docMediaType')
        if m.get('gmtModifiedTimestamp') is not None:
            self.gmt_modified_timestamp = m.get('gmtModifiedTimestamp')
        if m.get('mediaName') is not None:
            self.media_name = m.get('mediaName')
        if m.get('memos') is not None:
            self.memos = m.get('memos')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('modifierOutNo') is not None:
            self.modifier_out_no = m.get('modifierOutNo')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('selfContentSignStr') is not None:
            self.self_content_sign_str = m.get('selfContentSignStr')
        if m.get('sourceUrl') is not None:
            self.source_url = m.get('sourceUrl')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('message') is not None:
            temp_model = YuqingMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class AlarmQueryCondition(TeaModel):
    def __init__(
        self,
        alarm_rule_id: List[int] = None,
        doc_ids: List[int] = None,
        doc_media_type: List[str] = None,
        end_time: int = None,
        ids: List[int] = None,
        levels: List[str] = None,
        page_now: int = None,
        page_size: int = None,
        projec_ids: List[int] = None,
        start_time: int = None,
        status: List[str] = None,
        tag_ids: List[int] = None,
        type: str = None,
        is_query_update_time: bool = None,
    ):
        # 规则id列表
        self.alarm_rule_id = alarm_rule_id
        # 舆情消息id列表
        self.doc_ids = doc_ids
        # 查询数据的消息类型
        self.doc_media_type = doc_media_type
        # 查询结束时间,毫秒
        self.end_time = end_time
        # 预警id列表
        self.ids = ids
        # 预警等级过滤列表
        self.levels = levels
        # 当前页
        self.page_now = page_now
        # 分页大小
        self.page_size = page_size
        # 舆情项目id
        self.projec_ids = projec_ids
        # 查询开始时间,毫秒
        self.start_time = start_time
        # 预警状态列表
        self.status = status
        # 标签id列表
        self.tag_ids = tag_ids
        # 预警规则类型
        self.type = type
        # 是否使用更新时间作为筛选
        self.is_query_update_time = is_query_update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alarm_rule_id is not None:
            result['alarmRuleId'] = self.alarm_rule_id
        if self.doc_ids is not None:
            result['docIds'] = self.doc_ids
        if self.doc_media_type is not None:
            result['docMediaType'] = self.doc_media_type
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.ids is not None:
            result['ids'] = self.ids
        if self.levels is not None:
            result['levels'] = self.levels
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.projec_ids is not None:
            result['projecIds'] = self.projec_ids
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.tag_ids is not None:
            result['tagIds'] = self.tag_ids
        if self.type is not None:
            result['type'] = self.type
        if self.is_query_update_time is not None:
            result['isQueryUpdateTime'] = self.is_query_update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmRuleId') is not None:
            self.alarm_rule_id = m.get('alarmRuleId')
        if m.get('docIds') is not None:
            self.doc_ids = m.get('docIds')
        if m.get('docMediaType') is not None:
            self.doc_media_type = m.get('docMediaType')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        if m.get('levels') is not None:
            self.levels = m.get('levels')
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projecIds') is not None:
            self.projec_ids = m.get('projecIds')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tagIds') is not None:
            self.tag_ids = m.get('tagIds')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('isQueryUpdateTime') is not None:
            self.is_query_update_time = m.get('isQueryUpdateTime')
        return self


class QueryAlarmDataListRequest(TeaModel):
    def __init__(
        self,
        alarm_query: AlarmQueryCondition = None,
        order_by_key: str = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        self.alarm_query = alarm_query
        # 排序方式
        self.order_by_key = order_by_key
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        if self.alarm_query:
            self.alarm_query.validate()

    def to_map(self):
        result = dict()
        if self.alarm_query is not None:
            result['alarmQuery'] = self.alarm_query.to_map()
        if self.order_by_key is not None:
            result['orderByKey'] = self.order_by_key
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alarmQuery') is not None:
            temp_model = AlarmQueryCondition()
            self.alarm_query = temp_model.from_map(m['alarmQuery'])
        if m.get('orderByKey') is not None:
            self.order_by_key = m.get('orderByKey')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryAlarmDataListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        pages: List[AlarmData] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 预警列表
        self.pages = pages
        # 总条数
        self.total_count = total_count

    def validate(self):
        if self.pages:
            for k in self.pages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['pages'] = []
        if self.pages is not None:
            for k in self.pages:
                result['pages'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.pages = []
        if m.get('pages') is not None:
            for k in m.get('pages'):
                temp_model = AlarmData()
                self.pages.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryAlarmDataListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAlarmDataListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryAlarmDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAnalysisComponentResultRequest(TeaModel):
    def __init__(
        self,
        analysis_id: int = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 分析任务Id
        self.analysis_id = analysis_id
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetAnalysisComponentResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_json: str = None,
        analysis_id: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 任务结果json。参考opinion.analysis.component.query的result_json
        self.result_json = result_json
        # 任务Id
        self.analysis_id = analysis_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result_json is not None:
            result['resultJson'] = self.result_json
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resultJson') is not None:
            self.result_json = m.get('resultJson')
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        return self


class GetAnalysisComponentResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAnalysisComponentResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetAnalysisComponentResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageDetailRequest(TeaModel):
    def __init__(
        self,
        doc_id: str = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 舆情文章Id
        self.doc_id = doc_id
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetMessageDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 舆情消息体
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class GetMessageDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMessageDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetMessageDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        create_user_id: str = None,
        create_user_name: str = None,
        project: Project = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 创建者uid
        self.create_user_id = create_user_id
        # 创建者名称
        self.create_user_name = create_user_name
        # 舆情项目对象
        self.project = project
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        if self.create_user_id is not None:
            result['createUserId'] = self.create_user_id
        if self.create_user_name is not None:
            result['createUserName'] = self.create_user_name
        if self.project is not None:
            result['project'] = self.project.to_map()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createUserId') is not None:
            self.create_user_id = m.get('createUserId')
        if m.get('createUserName') is not None:
            self.create_user_name = m.get('createUserName')
        if m.get('project') is not None:
            temp_model = Project()
            self.project = temp_model.from_map(m['project'])
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        # 舆情项目id
        self.id = id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
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


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProjectListRequest(TeaModel):
    def __init__(
        self,
        page_now: int = None,
        page_size: int = None,
        project_group_id: int = None,
        project_id: int = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 当前页数，从1开始
        self.page_now = page_now
        # 分页大小
        self.page_size = page_size
        # 所属项目分组id
        self.project_group_id = project_group_id
        # 指定舆情项目id
        self.project_id = project_id
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_group_id is not None:
            result['projectGroupId'] = self.project_group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectGroupId') is not None:
            self.project_group_id = m.get('projectGroupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryProjectListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        project_list: List[Project] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 舆情项目列表,参考Project对象
        self.project_list = project_list
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.project_list:
            for k in self.project_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['projectList'] = []
        if self.project_list is not None:
            for k in self.project_list:
                result['projectList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.project_list = []
        if m.get('projectList') is not None:
            for k in m.get('projectList'):
                temp_model = Project()
                self.project_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryProjectListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryProjectListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryProjectListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagNodesRequest(TeaModel):
    def __init__(
        self,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryTagNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        biz_tag_tree_list: List[BizTagTree] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 标签列表
        self.biz_tag_tree_list = biz_tag_tree_list

    def validate(self):
        if self.biz_tag_tree_list:
            for k in self.biz_tag_tree_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['bizTagTreeList'] = []
        if self.biz_tag_tree_list is not None:
            for k in self.biz_tag_tree_list:
                result['bizTagTreeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.biz_tag_tree_list = []
        if m.get('bizTagTreeList') is not None:
            for k in m.get('bizTagTreeList'):
                temp_model = BizTagTree()
                self.biz_tag_tree_list.append(temp_model.from_map(k))
        return self


class QueryTagNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTagNodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryTagNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryReportNotifiesRequest(TeaModel):
    def __init__(
        self,
        cp_id: int = None,
        create_end_timestamp: int = None,
        create_start_timestamp: int = None,
        page_now: int = None,
        page_size: int = None,
        subject: str = None,
        type: int = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 自定义页面id
        self.cp_id = cp_id
        # 创建截止时间,毫秒
        self.create_end_timestamp = create_end_timestamp
        # 创建开始时间，毫秒
        self.create_start_timestamp = create_start_timestamp
        # 当前页数，从1开始
        self.page_now = page_now
        # 分页大小
        self.page_size = page_size
        # 主题
        self.subject = subject
        # 类型： 如邮件、钉钉等
        self.type = type
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cp_id is not None:
            result['cpId'] = self.cp_id
        if self.create_end_timestamp is not None:
            result['createEndTimestamp'] = self.create_end_timestamp
        if self.create_start_timestamp is not None:
            result['createStartTimestamp'] = self.create_start_timestamp
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.subject is not None:
            result['subject'] = self.subject
        if self.type is not None:
            result['type'] = self.type
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpId') is not None:
            self.cp_id = m.get('cpId')
        if m.get('createEndTimestamp') is not None:
            self.create_end_timestamp = m.get('createEndTimestamp')
        if m.get('createStartTimestamp') is not None:
            self.create_start_timestamp = m.get('createStartTimestamp')
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryReportNotifiesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        report_notify_record_list: List[ReportNotifyRecord] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 报告历史发送信息
        self.report_notify_record_list = report_notify_record_list
        # 总数量
        self.total_count = total_count

    def validate(self):
        if self.report_notify_record_list:
            for k in self.report_notify_record_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['reportNotifyRecordList'] = []
        if self.report_notify_record_list is not None:
            for k in self.report_notify_record_list:
                result['reportNotifyRecordList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.report_notify_record_list = []
        if m.get('reportNotifyRecordList') is not None:
            for k in m.get('reportNotifyRecordList'):
                temp_model = ReportNotifyRecord()
                self.report_notify_record_list.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryReportNotifiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryReportNotifiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryReportNotifiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        modified_user_id: str = None,
        modified_user_name: str = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 舆情项目id
        self.id = id
        # 修改人uid
        self.modified_user_id = modified_user_id
        # 修改人名称
        self.modified_user_name = modified_user_name
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.modified_user_id is not None:
            result['modifiedUserId'] = self.modified_user_id
        if self.modified_user_name is not None:
            result['modifiedUserName'] = self.modified_user_name
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifiedUserId') is not None:
            self.modified_user_id = m.get('modifiedUserId')
        if m.get('modifiedUserName') is not None:
            self.modified_user_name = m.get('modifiedUserName')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        # 被删除的项目id
        self.id = id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
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


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFilterListRequest(TeaModel):
    def __init__(
        self,
        page_now: int = None,
        page_size: int = None,
        filter_id: int = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 当前查询的第几页，从1开始
        self.page_now = page_now
        # 查询每页的数据量
        self.page_size = page_size
        # 指定筛选模板id查询
        self.filter_id = filter_id
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_now is not None:
            result['pageNow'] = self.page_now
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.filter_id is not None:
            result['filterId'] = self.filter_id
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNow') is not None:
            self.page_now = m.get('pageNow')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('filterId') is not None:
            self.filter_id = m.get('filterId')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryFilterListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        filters: List[Filter] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 筛选模板列表。
        self.filters = filters
        # 总条数
        self.total_count = total_count

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['filters'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.filters = []
        if m.get('filters') is not None:
            for k in m.get('filters'):
                temp_model = Filter()
                self.filters.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class QueryFilterListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryFilterListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryFilterListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AggregateSearchYuqingRequest(TeaModel):
    def __init__(
        self,
        search_condition: SearchCondition = None,
        aggregate_function: str = None,
        group_by_key: str = None,
        group_limits: int = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 查询舆情条件
        self.search_condition = search_condition
        # 聚合函数
        self.aggregate_function = aggregate_function
        # 聚合字段名字,枚举值
        self.group_by_key = group_by_key
        # 聚合结果条数
        self.group_limits = group_limits
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        if self.search_condition:
            self.search_condition.validate()

    def to_map(self):
        result = dict()
        if self.search_condition is not None:
            result['searchCondition'] = self.search_condition.to_map()
        if self.aggregate_function is not None:
            result['aggregateFunction'] = self.aggregate_function
        if self.group_by_key is not None:
            result['groupByKey'] = self.group_by_key
        if self.group_limits is not None:
            result['groupLimits'] = self.group_limits
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('searchCondition') is not None:
            temp_model = SearchCondition()
            self.search_condition = temp_model.from_map(m['searchCondition'])
        if m.get('aggregateFunction') is not None:
            self.aggregate_function = m.get('aggregateFunction')
        if m.get('groupByKey') is not None:
            self.group_by_key = m.get('groupByKey')
        if m.get('groupLimits') is not None:
            self.group_limits = m.get('groupLimits')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AggregateSearchYuqingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        agg_result_list: List[StatisticPoint] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 聚合结果列表
        self.agg_result_list = agg_result_list

    def validate(self):
        if self.agg_result_list:
            for k in self.agg_result_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['aggResultList'] = []
        if self.agg_result_list is not None:
            for k in self.agg_result_list:
                result['aggResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.agg_result_list = []
        if m.get('aggResultList') is not None:
            for k in m.get('aggResultList'):
                temp_model = StatisticPoint()
                self.agg_result_list.append(temp_model.from_map(k))
        return self


class AggregateSearchYuqingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AggregateSearchYuqingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AggregateSearchYuqingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAnalysisComponentRequest(TeaModel):
    def __init__(
        self,
        analyse_type: str = None,
        search_condition: SearchCondition = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 分析任务类型名称，具体可以填写的值可以在舆情平台查看
        self.analyse_type = analyse_type
        # 搜索舆情条件
        self.search_condition = search_condition
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        if self.search_condition:
            self.search_condition.validate()

    def to_map(self):
        result = dict()
        if self.analyse_type is not None:
            result['analyseType'] = self.analyse_type
        if self.search_condition is not None:
            result['searchCondition'] = self.search_condition.to_map()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyseType') is not None:
            self.analyse_type = m.get('analyseType')
        if m.get('searchCondition') is not None:
            temp_model = SearchCondition()
            self.search_condition = temp_model.from_map(m['searchCondition'])
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryAnalysisComponentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        analysis_id: int = None,
        result_json: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 分析任务Id，用于查询这个任务对应的结果。如果是快速完成类型的分析，会直接返回结果。如果无结果返回，业务方可以根据这个id轮询查询结果。
        self.analysis_id = analysis_id
        # 分析任务返回的结果json字符串，不同分析任务返回的json格式不一样。
        self.result_json = result_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        if self.result_json is not None:
            result['resultJson'] = self.result_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        if m.get('resultJson') is not None:
            self.result_json = m.get('resultJson')
        return self


class QueryAnalysisComponentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAnalysisComponentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = QueryAnalysisComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePropagationRequest(TeaModel):
    def __init__(
        self,
        weibo_urls: List[str] = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 微博源地址
        self.weibo_urls = weibo_urls
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.weibo_urls is not None:
            result['weiboUrls'] = self.weibo_urls
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('weiboUrls') is not None:
            self.weibo_urls = m.get('weiboUrls')
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdatePropagationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdatePropagationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePropagationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdatePropagationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListYuqingMessagesRequest(TeaModel):
    def __init__(
        self,
        search_condition: SearchCondition = None,
        team_hash_id: str = None,
        request_id: str = None,
    ):
        # 查询过滤参数，多个过滤参数之间是且的关系。例如:过滤实例名称为i-a123、i-b123，且实例状态为Stopped：&Filter.1.Name=InstanceName&Filter.1.Value.1=i-a123&Filter.1.Value.2=i-b123&Filter.2.Name=Status&Filter.2.Value=Stopped。
        self.search_condition = search_condition
        # 舆情团队HashId
        self.team_hash_id = team_hash_id
        # 请求id
        self.request_id = request_id

    def validate(self):
        if self.search_condition:
            self.search_condition.validate()

    def to_map(self):
        result = dict()
        if self.search_condition is not None:
            result['searchCondition'] = self.search_condition.to_map()
        if self.team_hash_id is not None:
            result['teamHashId'] = self.team_hash_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('searchCondition') is not None:
            temp_model = SearchCondition()
            self.search_condition = temp_model.from_map(m['searchCondition'])
        if m.get('teamHashId') is not None:
            self.team_hash_id = m.get('teamHashId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListYuqingMessagesResponseBody(TeaModel):
    def __init__(
        self,
        yuqing_messages: List[YuqingMessage] = None,
        total_count: int = None,
        request_id: str = None,
    ):
        # 数组，返回示例目录。
        self.yuqing_messages = yuqing_messages
        # 总记录数。
        self.total_count = total_count
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.yuqing_messages:
            for k in self.yuqing_messages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['yuqingMessages'] = []
        if self.yuqing_messages is not None:
            for k in self.yuqing_messages:
                result['yuqingMessages'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.yuqing_messages = []
        if m.get('yuqingMessages') is not None:
            for k in m.get('yuqingMessages'):
                temp_model = YuqingMessage()
                self.yuqing_messages.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListYuqingMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListYuqingMessagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = ListYuqingMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


