# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ConsoleBody(TeaModel):
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


class FieldCondition(TeaModel):
    def __init__(
        self,
        field_name: str = None,
        nest_field_path: str = None,
        nest_field_value: List[int] = None,
        operate_type: str = None,
        value: str = None,
    ):
        self.field_name = field_name
        self.nest_field_path = nest_field_path
        self.nest_field_value = nest_field_value
        self.operate_type = operate_type
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
        # This parameter is required.
        self.app_code = app_code
        self.buyer_name = buyer_name
        # This parameter is required.
        self.buyer_uid = buyer_uid
        # This parameter is required.
        self.channel = channel
        self.config = config
        self.end = end
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.order_no = order_no
        # This parameter is required.
        self.product_code = product_code
        # This parameter is required.
        self.product_spec_code = product_spec_code
        self.start = start
        self.tenant_name = tenant_name
        # This parameter is required.
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
        exclude_material_tag_list: List[str] = None,
        exclude_media_library_id_list: List[str] = None,
        exclude_media_name_list: List[str] = None,
        exclude_media_type_list: List[str] = None,
        exclude_message_type_list: List[str] = None,
        field_conditions: List[FieldCondition] = None,
        filter_id: int = None,
        has_audio: bool = None,
        has_image: bool = None,
        has_multi_mode_content: bool = None,
        has_video: bool = None,
        host_name_list: List[str] = None,
        influence_level: int = None,
        keyword_tag_ids: List[int] = None,
        likes_level: int = None,
        material_tag_list: List[str] = None,
        media_library_id_list: List[str] = None,
        media_name_list: List[str] = None,
        media_type_list: List[str] = None,
        message_type_list: List[str] = None,
        page_now: int = None,
        page_size: int = None,
        parent_doc_id: str = None,
        pos_keyword_list: List[str] = None,
        pos_keyword_list_in_title: List[str] = None,
        project_id: int = None,
        propagation_level: int = None,
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
        self.ass_keyword_list = ass_keyword_list
        self.at_author_name_list = at_author_name_list
        self.author_name_list = author_name_list
        self.comments_level = comments_level
        self.content_len_level = content_len_level
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.doc_content_sign = doc_content_sign
        self.doc_id_list = doc_id_list
        self.duplicate_removal = duplicate_removal
        self.emotion_type = emotion_type
        self.enable_keyword_highlight = enable_keyword_highlight
        self.exclude_at_author_name_list = exclude_at_author_name_list
        self.exclude_author_name_list = exclude_author_name_list
        self.exclude_host_name_list = exclude_host_name_list
        self.exclude_keyword_list = exclude_keyword_list
        self.exclude_keyword_list_in_title = exclude_keyword_list_in_title
        self.exclude_keyword_tag_ids = exclude_keyword_tag_ids
        self.exclude_material_tag_list = exclude_material_tag_list
        self.exclude_media_library_id_list = exclude_media_library_id_list
        self.exclude_media_name_list = exclude_media_name_list
        self.exclude_media_type_list = exclude_media_type_list
        self.exclude_message_type_list = exclude_message_type_list
        self.field_conditions = field_conditions
        self.filter_id = filter_id
        self.has_audio = has_audio
        self.has_image = has_image
        self.has_multi_mode_content = has_multi_mode_content
        self.has_video = has_video
        self.host_name_list = host_name_list
        self.influence_level = influence_level
        self.keyword_tag_ids = keyword_tag_ids
        self.likes_level = likes_level
        self.material_tag_list = material_tag_list
        self.media_library_id_list = media_library_id_list
        self.media_name_list = media_name_list
        self.media_type_list = media_type_list
        self.message_type_list = message_type_list
        self.page_now = page_now
        self.page_size = page_size
        self.parent_doc_id = parent_doc_id
        self.pos_keyword_list = pos_keyword_list
        self.pos_keyword_list_in_title = pos_keyword_list_in_title
        self.project_id = project_id
        self.propagation_level = propagation_level
        self.publish_time_end = publish_time_end
        self.publish_time_start = publish_time_start
        self.reads_level = reads_level
        self.relevance_level = relevance_level
        self.repost_level = repost_level
        self.sort_by = sort_by
        self.sort_by_direction = sort_by_direction
        self.topic_list = topic_list
        self.update_time_end = update_time_end
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
        if self.exclude_material_tag_list is not None:
            result['excludeMaterialTagList'] = self.exclude_material_tag_list
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
        if self.filter_id is not None:
            result['filterId'] = self.filter_id
        if self.has_audio is not None:
            result['hasAudio'] = self.has_audio
        if self.has_image is not None:
            result['hasImage'] = self.has_image
        if self.has_multi_mode_content is not None:
            result['hasMultiModeContent'] = self.has_multi_mode_content
        if self.has_video is not None:
            result['hasVideo'] = self.has_video
        if self.host_name_list is not None:
            result['hostNameList'] = self.host_name_list
        if self.influence_level is not None:
            result['influenceLevel'] = self.influence_level
        if self.keyword_tag_ids is not None:
            result['keywordTagIds'] = self.keyword_tag_ids
        if self.likes_level is not None:
            result['likesLevel'] = self.likes_level
        if self.material_tag_list is not None:
            result['materialTagList'] = self.material_tag_list
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
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.propagation_level is not None:
            result['propagationLevel'] = self.propagation_level
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
        if m.get('excludeMaterialTagList') is not None:
            self.exclude_material_tag_list = m.get('excludeMaterialTagList')
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
        if m.get('filterId') is not None:
            self.filter_id = m.get('filterId')
        if m.get('hasAudio') is not None:
            self.has_audio = m.get('hasAudio')
        if m.get('hasImage') is not None:
            self.has_image = m.get('hasImage')
        if m.get('hasMultiModeContent') is not None:
            self.has_multi_mode_content = m.get('hasMultiModeContent')
        if m.get('hasVideo') is not None:
            self.has_video = m.get('hasVideo')
        if m.get('hostNameList') is not None:
            self.host_name_list = m.get('hostNameList')
        if m.get('influenceLevel') is not None:
            self.influence_level = m.get('influenceLevel')
        if m.get('keywordTagIds') is not None:
            self.keyword_tag_ids = m.get('keywordTagIds')
        if m.get('likesLevel') is not None:
            self.likes_level = m.get('likesLevel')
        if m.get('materialTagList') is not None:
            self.material_tag_list = m.get('materialTagList')
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
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('propagationLevel') is not None:
            self.propagation_level = m.get('propagationLevel')
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


class YuqingFinanceEvent(TeaModel):
    def __init__(
        self,
        comprehensive_risk: float = None,
        entity_area: str = None,
        entity_crn: str = None,
        entity_emotion_score: float = None,
        entity_id: int = None,
        entity_name: str = None,
        entity_relevance_score: float = None,
        entity_show_name: str = None,
        entity_summary: str = None,
        entity_type: str = None,
        event_id: str = None,
        event_level_3code: int = None,
        event_level_3name: str = None,
        event_tags: str = None,
        event_time: int = None,
        security_abbreviation: str = None,
        security_category_codes: List[str] = None,
        security_codes: List[str] = None,
        security_markets_codes: List[str] = None,
        spam_score: float = None,
        user_subscribe_entity_tags: List[str] = None,
        user_subscribe_event_tags: List[int] = None,
    ):
        self.comprehensive_risk = comprehensive_risk
        self.entity_area = entity_area
        self.entity_crn = entity_crn
        self.entity_emotion_score = entity_emotion_score
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_relevance_score = entity_relevance_score
        self.entity_show_name = entity_show_name
        self.entity_summary = entity_summary
        self.entity_type = entity_type
        self.event_id = event_id
        self.event_level_3code = event_level_3code
        self.event_level_3name = event_level_3name
        self.event_tags = event_tags
        self.event_time = event_time
        self.security_abbreviation = security_abbreviation
        self.security_category_codes = security_category_codes
        self.security_codes = security_codes
        self.security_markets_codes = security_markets_codes
        self.spam_score = spam_score
        self.user_subscribe_entity_tags = user_subscribe_entity_tags
        self.user_subscribe_event_tags = user_subscribe_event_tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comprehensive_risk is not None:
            result['comprehensiveRisk'] = self.comprehensive_risk
        if self.entity_area is not None:
            result['entityArea'] = self.entity_area
        if self.entity_crn is not None:
            result['entityCrn'] = self.entity_crn
        if self.entity_emotion_score is not None:
            result['entityEmotionScore'] = self.entity_emotion_score
        if self.entity_id is not None:
            result['entityId'] = self.entity_id
        if self.entity_name is not None:
            result['entityName'] = self.entity_name
        if self.entity_relevance_score is not None:
            result['entityRelevanceScore'] = self.entity_relevance_score
        if self.entity_show_name is not None:
            result['entityShowName'] = self.entity_show_name
        if self.entity_summary is not None:
            result['entitySummary'] = self.entity_summary
        if self.entity_type is not None:
            result['entityType'] = self.entity_type
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.event_level_3code is not None:
            result['eventLevel3Code'] = self.event_level_3code
        if self.event_level_3name is not None:
            result['eventLevel3Name'] = self.event_level_3name
        if self.event_tags is not None:
            result['eventTags'] = self.event_tags
        if self.event_time is not None:
            result['eventTime'] = self.event_time
        if self.security_abbreviation is not None:
            result['securityAbbreviation'] = self.security_abbreviation
        if self.security_category_codes is not None:
            result['securityCategoryCodes'] = self.security_category_codes
        if self.security_codes is not None:
            result['securityCodes'] = self.security_codes
        if self.security_markets_codes is not None:
            result['securityMarketsCodes'] = self.security_markets_codes
        if self.spam_score is not None:
            result['spamScore'] = self.spam_score
        if self.user_subscribe_entity_tags is not None:
            result['userSubscribeEntityTags'] = self.user_subscribe_entity_tags
        if self.user_subscribe_event_tags is not None:
            result['userSubscribeEventTags'] = self.user_subscribe_event_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comprehensiveRisk') is not None:
            self.comprehensive_risk = m.get('comprehensiveRisk')
        if m.get('entityArea') is not None:
            self.entity_area = m.get('entityArea')
        if m.get('entityCrn') is not None:
            self.entity_crn = m.get('entityCrn')
        if m.get('entityEmotionScore') is not None:
            self.entity_emotion_score = m.get('entityEmotionScore')
        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')
        if m.get('entityName') is not None:
            self.entity_name = m.get('entityName')
        if m.get('entityRelevanceScore') is not None:
            self.entity_relevance_score = m.get('entityRelevanceScore')
        if m.get('entityShowName') is not None:
            self.entity_show_name = m.get('entityShowName')
        if m.get('entitySummary') is not None:
            self.entity_summary = m.get('entitySummary')
        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('eventLevel3Code') is not None:
            self.event_level_3code = m.get('eventLevel3Code')
        if m.get('eventLevel3Name') is not None:
            self.event_level_3name = m.get('eventLevel3Name')
        if m.get('eventTags') is not None:
            self.event_tags = m.get('eventTags')
        if m.get('eventTime') is not None:
            self.event_time = m.get('eventTime')
        if m.get('securityAbbreviation') is not None:
            self.security_abbreviation = m.get('securityAbbreviation')
        if m.get('securityCategoryCodes') is not None:
            self.security_category_codes = m.get('securityCategoryCodes')
        if m.get('securityCodes') is not None:
            self.security_codes = m.get('securityCodes')
        if m.get('securityMarketsCodes') is not None:
            self.security_markets_codes = m.get('securityMarketsCodes')
        if m.get('spamScore') is not None:
            self.spam_score = m.get('spamScore')
        if m.get('userSubscribeEntityTags') is not None:
            self.user_subscribe_entity_tags = m.get('userSubscribeEntityTags')
        if m.get('userSubscribeEventTags') is not None:
            self.user_subscribe_event_tags = m.get('userSubscribeEventTags')
        return self


class YuqingMessage(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_score: int = None,
        app_store_name: str = None,
        at_author_names: List[str] = None,
        audio_count: int = None,
        author_avatar_url: str = None,
        author_followers_count: int = None,
        author_friends_count: int = None,
        author_gender: str = None,
        author_id: str = None,
        author_likes_count: int = None,
        author_name: str = None,
        author_profile_url: str = None,
        author_statuses_count: int = None,
        author_verified: bool = None,
        author_verify_type: int = None,
        content_audio_text: str = None,
        content_audio_urls: str = None,
        content_image_text: str = None,
        content_image_urls: str = None,
        content_lang: str = None,
        content_len: int = None,
        content_video_text: str = None,
        content_video_urls: str = None,
        create_time: int = None,
        doc_answers_count: int = None,
        doc_areas: List[str] = None,
        doc_coin_count: int = None,
        doc_comments_count: int = None,
        doc_content: str = None,
        doc_content_brief: str = None,
        doc_content_sign: str = None,
        doc_id: str = None,
        doc_likes_count: int = None,
        doc_play_count: int = None,
        doc_reading_count: int = None,
        doc_reads_count: int = None,
        doc_reposts_count: int = None,
        doc_reprint_name: str = None,
        doc_self_content_sign: str = None,
        doc_title: str = None,
        doc_url: str = None,
        emotion_score: float = None,
        emotion_type: int = None,
        ext_info: Dict[str, str] = None,
        fin_event_count: int = None,
        finance_event_list: List[YuqingFinanceEvent] = None,
        highlight_keywords: List[str] = None,
        image_count: int = None,
        influence_score: float = None,
        media_hosts: List[str] = None,
        media_influence_level: int = None,
        media_name: str = None,
        media_propagation_level: int = None,
        media_type: str = None,
        message_type: str = None,
        parent_doc_id: str = None,
        propagation_score: float = None,
        publish_time: int = None,
        relevance_score: float = None,
        report_material_tags: List[str] = None,
        repost_list: List[str] = None,
        similar_number: int = None,
        topics: List[str] = None,
        video_count: int = None,
        weibo_comment_id: str = None,
        weibo_mid: str = None,
    ):
        self.app_name = app_name
        self.app_score = app_score
        self.app_store_name = app_store_name
        self.at_author_names = at_author_names
        self.audio_count = audio_count
        self.author_avatar_url = author_avatar_url
        self.author_followers_count = author_followers_count
        self.author_friends_count = author_friends_count
        self.author_gender = author_gender
        self.author_id = author_id
        self.author_likes_count = author_likes_count
        self.author_name = author_name
        self.author_profile_url = author_profile_url
        self.author_statuses_count = author_statuses_count
        self.author_verified = author_verified
        self.author_verify_type = author_verify_type
        self.content_audio_text = content_audio_text
        self.content_audio_urls = content_audio_urls
        self.content_image_text = content_image_text
        self.content_image_urls = content_image_urls
        self.content_lang = content_lang
        self.content_len = content_len
        self.content_video_text = content_video_text
        self.content_video_urls = content_video_urls
        self.create_time = create_time
        self.doc_answers_count = doc_answers_count
        self.doc_areas = doc_areas
        self.doc_coin_count = doc_coin_count
        self.doc_comments_count = doc_comments_count
        self.doc_content = doc_content
        self.doc_content_brief = doc_content_brief
        self.doc_content_sign = doc_content_sign
        self.doc_id = doc_id
        self.doc_likes_count = doc_likes_count
        self.doc_play_count = doc_play_count
        self.doc_reading_count = doc_reading_count
        self.doc_reads_count = doc_reads_count
        self.doc_reposts_count = doc_reposts_count
        self.doc_reprint_name = doc_reprint_name
        self.doc_self_content_sign = doc_self_content_sign
        self.doc_title = doc_title
        self.doc_url = doc_url
        self.emotion_score = emotion_score
        self.emotion_type = emotion_type
        self.ext_info = ext_info
        self.fin_event_count = fin_event_count
        self.finance_event_list = finance_event_list
        self.highlight_keywords = highlight_keywords
        self.image_count = image_count
        self.influence_score = influence_score
        self.media_hosts = media_hosts
        self.media_influence_level = media_influence_level
        self.media_name = media_name
        self.media_propagation_level = media_propagation_level
        self.media_type = media_type
        self.message_type = message_type
        self.parent_doc_id = parent_doc_id
        self.propagation_score = propagation_score
        self.publish_time = publish_time
        self.relevance_score = relevance_score
        self.report_material_tags = report_material_tags
        self.repost_list = repost_list
        self.similar_number = similar_number
        self.topics = topics
        self.video_count = video_count
        self.weibo_comment_id = weibo_comment_id
        self.weibo_mid = weibo_mid

    def validate(self):
        if self.finance_event_list:
            for k in self.finance_event_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.app_score is not None:
            result['appScore'] = self.app_score
        if self.app_store_name is not None:
            result['appStoreName'] = self.app_store_name
        if self.at_author_names is not None:
            result['atAuthorNames'] = self.at_author_names
        if self.audio_count is not None:
            result['audioCount'] = self.audio_count
        if self.author_avatar_url is not None:
            result['authorAvatarUrl'] = self.author_avatar_url
        if self.author_followers_count is not None:
            result['authorFollowersCount'] = self.author_followers_count
        if self.author_friends_count is not None:
            result['authorFriendsCount'] = self.author_friends_count
        if self.author_gender is not None:
            result['authorGender'] = self.author_gender
        if self.author_id is not None:
            result['authorId'] = self.author_id
        if self.author_likes_count is not None:
            result['authorLikesCount'] = self.author_likes_count
        if self.author_name is not None:
            result['authorName'] = self.author_name
        if self.author_profile_url is not None:
            result['authorProfileUrl'] = self.author_profile_url
        if self.author_statuses_count is not None:
            result['authorStatusesCount'] = self.author_statuses_count
        if self.author_verified is not None:
            result['authorVerified'] = self.author_verified
        if self.author_verify_type is not None:
            result['authorVerifyType'] = self.author_verify_type
        if self.content_audio_text is not None:
            result['contentAudioText'] = self.content_audio_text
        if self.content_audio_urls is not None:
            result['contentAudioUrls'] = self.content_audio_urls
        if self.content_image_text is not None:
            result['contentImageText'] = self.content_image_text
        if self.content_image_urls is not None:
            result['contentImageUrls'] = self.content_image_urls
        if self.content_lang is not None:
            result['contentLang'] = self.content_lang
        if self.content_len is not None:
            result['contentLen'] = self.content_len
        if self.content_video_text is not None:
            result['contentVideoText'] = self.content_video_text
        if self.content_video_urls is not None:
            result['contentVideoUrls'] = self.content_video_urls
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.doc_answers_count is not None:
            result['docAnswersCount'] = self.doc_answers_count
        if self.doc_areas is not None:
            result['docAreas'] = self.doc_areas
        if self.doc_coin_count is not None:
            result['docCoinCount'] = self.doc_coin_count
        if self.doc_comments_count is not None:
            result['docCommentsCount'] = self.doc_comments_count
        if self.doc_content is not None:
            result['docContent'] = self.doc_content
        if self.doc_content_brief is not None:
            result['docContentBrief'] = self.doc_content_brief
        if self.doc_content_sign is not None:
            result['docContentSign'] = self.doc_content_sign
        if self.doc_id is not None:
            result['docId'] = self.doc_id
        if self.doc_likes_count is not None:
            result['docLikesCount'] = self.doc_likes_count
        if self.doc_play_count is not None:
            result['docPlayCount'] = self.doc_play_count
        if self.doc_reading_count is not None:
            result['docReadingCount'] = self.doc_reading_count
        if self.doc_reads_count is not None:
            result['docReadsCount'] = self.doc_reads_count
        if self.doc_reposts_count is not None:
            result['docRepostsCount'] = self.doc_reposts_count
        if self.doc_reprint_name is not None:
            result['docReprintName'] = self.doc_reprint_name
        if self.doc_self_content_sign is not None:
            result['docSelfContentSign'] = self.doc_self_content_sign
        if self.doc_title is not None:
            result['docTitle'] = self.doc_title
        if self.doc_url is not None:
            result['docUrl'] = self.doc_url
        if self.emotion_score is not None:
            result['emotionScore'] = self.emotion_score
        if self.emotion_type is not None:
            result['emotionType'] = self.emotion_type
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.fin_event_count is not None:
            result['finEventCount'] = self.fin_event_count
        result['financeEventList'] = []
        if self.finance_event_list is not None:
            for k in self.finance_event_list:
                result['financeEventList'].append(k.to_map() if k else None)
        if self.highlight_keywords is not None:
            result['highlightKeywords'] = self.highlight_keywords
        if self.image_count is not None:
            result['imageCount'] = self.image_count
        if self.influence_score is not None:
            result['influenceScore'] = self.influence_score
        if self.media_hosts is not None:
            result['mediaHosts'] = self.media_hosts
        if self.media_influence_level is not None:
            result['mediaInfluenceLevel'] = self.media_influence_level
        if self.media_name is not None:
            result['mediaName'] = self.media_name
        if self.media_propagation_level is not None:
            result['mediaPropagationLevel'] = self.media_propagation_level
        if self.media_type is not None:
            result['mediaType'] = self.media_type
        if self.message_type is not None:
            result['messageType'] = self.message_type
        if self.parent_doc_id is not None:
            result['parentDocId'] = self.parent_doc_id
        if self.propagation_score is not None:
            result['propagationScore'] = self.propagation_score
        if self.publish_time is not None:
            result['publishTime'] = self.publish_time
        if self.relevance_score is not None:
            result['relevanceScore'] = self.relevance_score
        if self.report_material_tags is not None:
            result['reportMaterialTags'] = self.report_material_tags
        if self.repost_list is not None:
            result['repostList'] = self.repost_list
        if self.similar_number is not None:
            result['similarNumber'] = self.similar_number
        if self.topics is not None:
            result['topics'] = self.topics
        if self.video_count is not None:
            result['videoCount'] = self.video_count
        if self.weibo_comment_id is not None:
            result['weiboCommentId'] = self.weibo_comment_id
        if self.weibo_mid is not None:
            result['weiboMid'] = self.weibo_mid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('appScore') is not None:
            self.app_score = m.get('appScore')
        if m.get('appStoreName') is not None:
            self.app_store_name = m.get('appStoreName')
        if m.get('atAuthorNames') is not None:
            self.at_author_names = m.get('atAuthorNames')
        if m.get('audioCount') is not None:
            self.audio_count = m.get('audioCount')
        if m.get('authorAvatarUrl') is not None:
            self.author_avatar_url = m.get('authorAvatarUrl')
        if m.get('authorFollowersCount') is not None:
            self.author_followers_count = m.get('authorFollowersCount')
        if m.get('authorFriendsCount') is not None:
            self.author_friends_count = m.get('authorFriendsCount')
        if m.get('authorGender') is not None:
            self.author_gender = m.get('authorGender')
        if m.get('authorId') is not None:
            self.author_id = m.get('authorId')
        if m.get('authorLikesCount') is not None:
            self.author_likes_count = m.get('authorLikesCount')
        if m.get('authorName') is not None:
            self.author_name = m.get('authorName')
        if m.get('authorProfileUrl') is not None:
            self.author_profile_url = m.get('authorProfileUrl')
        if m.get('authorStatusesCount') is not None:
            self.author_statuses_count = m.get('authorStatusesCount')
        if m.get('authorVerified') is not None:
            self.author_verified = m.get('authorVerified')
        if m.get('authorVerifyType') is not None:
            self.author_verify_type = m.get('authorVerifyType')
        if m.get('contentAudioText') is not None:
            self.content_audio_text = m.get('contentAudioText')
        if m.get('contentAudioUrls') is not None:
            self.content_audio_urls = m.get('contentAudioUrls')
        if m.get('contentImageText') is not None:
            self.content_image_text = m.get('contentImageText')
        if m.get('contentImageUrls') is not None:
            self.content_image_urls = m.get('contentImageUrls')
        if m.get('contentLang') is not None:
            self.content_lang = m.get('contentLang')
        if m.get('contentLen') is not None:
            self.content_len = m.get('contentLen')
        if m.get('contentVideoText') is not None:
            self.content_video_text = m.get('contentVideoText')
        if m.get('contentVideoUrls') is not None:
            self.content_video_urls = m.get('contentVideoUrls')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('docAnswersCount') is not None:
            self.doc_answers_count = m.get('docAnswersCount')
        if m.get('docAreas') is not None:
            self.doc_areas = m.get('docAreas')
        if m.get('docCoinCount') is not None:
            self.doc_coin_count = m.get('docCoinCount')
        if m.get('docCommentsCount') is not None:
            self.doc_comments_count = m.get('docCommentsCount')
        if m.get('docContent') is not None:
            self.doc_content = m.get('docContent')
        if m.get('docContentBrief') is not None:
            self.doc_content_brief = m.get('docContentBrief')
        if m.get('docContentSign') is not None:
            self.doc_content_sign = m.get('docContentSign')
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')
        if m.get('docLikesCount') is not None:
            self.doc_likes_count = m.get('docLikesCount')
        if m.get('docPlayCount') is not None:
            self.doc_play_count = m.get('docPlayCount')
        if m.get('docReadingCount') is not None:
            self.doc_reading_count = m.get('docReadingCount')
        if m.get('docReadsCount') is not None:
            self.doc_reads_count = m.get('docReadsCount')
        if m.get('docRepostsCount') is not None:
            self.doc_reposts_count = m.get('docRepostsCount')
        if m.get('docReprintName') is not None:
            self.doc_reprint_name = m.get('docReprintName')
        if m.get('docSelfContentSign') is not None:
            self.doc_self_content_sign = m.get('docSelfContentSign')
        if m.get('docTitle') is not None:
            self.doc_title = m.get('docTitle')
        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')
        if m.get('emotionScore') is not None:
            self.emotion_score = m.get('emotionScore')
        if m.get('emotionType') is not None:
            self.emotion_type = m.get('emotionType')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('finEventCount') is not None:
            self.fin_event_count = m.get('finEventCount')
        self.finance_event_list = []
        if m.get('financeEventList') is not None:
            for k in m.get('financeEventList'):
                temp_model = YuqingFinanceEvent()
                self.finance_event_list.append(temp_model.from_map(k))
        if m.get('highlightKeywords') is not None:
            self.highlight_keywords = m.get('highlightKeywords')
        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')
        if m.get('influenceScore') is not None:
            self.influence_score = m.get('influenceScore')
        if m.get('mediaHosts') is not None:
            self.media_hosts = m.get('mediaHosts')
        if m.get('mediaInfluenceLevel') is not None:
            self.media_influence_level = m.get('mediaInfluenceLevel')
        if m.get('mediaName') is not None:
            self.media_name = m.get('mediaName')
        if m.get('mediaPropagationLevel') is not None:
            self.media_propagation_level = m.get('mediaPropagationLevel')
        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')
        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')
        if m.get('parentDocId') is not None:
            self.parent_doc_id = m.get('parentDocId')
        if m.get('propagationScore') is not None:
            self.propagation_score = m.get('propagationScore')
        if m.get('publishTime') is not None:
            self.publish_time = m.get('publishTime')
        if m.get('relevanceScore') is not None:
            self.relevance_score = m.get('relevanceScore')
        if m.get('reportMaterialTags') is not None:
            self.report_material_tags = m.get('reportMaterialTags')
        if m.get('repostList') is not None:
            self.repost_list = m.get('repostList')
        if m.get('similarNumber') is not None:
            self.similar_number = m.get('similarNumber')
        if m.get('topics') is not None:
            self.topics = m.get('topics')
        if m.get('videoCount') is not None:
            self.video_count = m.get('videoCount')
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
        status_code: int = None,
        body: CloseProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloseProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConsoleApiProxyRequest(TeaModel):
    def __init__(
        self,
        body: ConsoleBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ConsoleBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConsoleApiProxyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_json: str = None,
    ):
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


class ConsoleApiProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConsoleApiProxyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConsoleApiProxyResponseBody()
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
        status_code: int = None,
        body: ConsoleProxyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        status_code: int = None,
        body: GetAnalysisTaskResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        self.client_token = client_token
        self.product_instance = product_instance
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
        status_code: int = None,
        body: OpenProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        status_code: int = None,
        body: QueryProductInstanceListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        status_code: int = None,
        body: QueryYuqingMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        status_code: int = None,
        body: SubmitAnalysisTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SubmitAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


