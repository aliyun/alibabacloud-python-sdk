# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class DescribeDocResponseBody(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        category_id: int = None,
        config: str = None,
        create_time: str = None,
        create_user_id: int = None,
        create_user_name: str = None,
        doc_info: main_models.DescribeDocResponseBodyDocInfo = None,
        doc_metadata: List[main_models.DescribeDocResponseBodyDocMetadata] = None,
        doc_name: str = None,
        doc_tags: List[main_models.DescribeDocResponseBodyDocTags] = None,
        effect_status: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        meta: str = None,
        modify_time: str = None,
        modify_user_id: int = None,
        modify_user_name: str = None,
        process_can_retry: bool = None,
        process_message: str = None,
        process_status: int = None,
        request_id: str = None,
        start_date: str = None,
        status: int = None,
        title: str = None,
        url: str = None,
    ):
        self.biz_code = biz_code
        self.category_id = category_id
        self.config = config
        self.create_time = create_time
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.doc_info = doc_info
        self.doc_metadata = doc_metadata
        self.doc_name = doc_name
        self.doc_tags = doc_tags
        self.effect_status = effect_status
        self.end_date = end_date
        self.knowledge_id = knowledge_id
        self.meta = meta
        self.modify_time = modify_time
        self.modify_user_id = modify_user_id
        self.modify_user_name = modify_user_name
        self.process_can_retry = process_can_retry
        self.process_message = process_message
        self.process_status = process_status
        # Id of the request
        self.request_id = request_id
        self.start_date = start_date
        self.status = status
        self.title = title
        self.url = url

    def validate(self):
        if self.doc_info:
            self.doc_info.validate()
        if self.doc_metadata:
            for v1 in self.doc_metadata:
                 if v1:
                    v1.validate()
        if self.doc_tags:
            for v1 in self.doc_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.config is not None:
            result['Config'] = self.config

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.doc_info is not None:
            result['DocInfo'] = self.doc_info.to_map()

        result['DocMetadata'] = []
        if self.doc_metadata is not None:
            for k1 in self.doc_metadata:
                result['DocMetadata'].append(k1.to_map() if k1 else None)

        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        result['DocTags'] = []
        if self.doc_tags is not None:
            for k1 in self.doc_tags:
                result['DocTags'].append(k1.to_map() if k1 else None)

        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.meta is not None:
            result['Meta'] = self.meta

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user_id is not None:
            result['ModifyUserId'] = self.modify_user_id

        if self.modify_user_name is not None:
            result['ModifyUserName'] = self.modify_user_name

        if self.process_can_retry is not None:
            result['ProcessCanRetry'] = self.process_can_retry

        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message

        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('DocInfo') is not None:
            temp_model = main_models.DescribeDocResponseBodyDocInfo()
            self.doc_info = temp_model.from_map(m.get('DocInfo'))

        self.doc_metadata = []
        if m.get('DocMetadata') is not None:
            for k1 in m.get('DocMetadata'):
                temp_model = main_models.DescribeDocResponseBodyDocMetadata()
                self.doc_metadata.append(temp_model.from_map(k1))

        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        self.doc_tags = []
        if m.get('DocTags') is not None:
            for k1 in m.get('DocTags'):
                temp_model = main_models.DescribeDocResponseBodyDocTags()
                self.doc_tags.append(temp_model.from_map(k1))

        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUserId') is not None:
            self.modify_user_id = m.get('ModifyUserId')

        if m.get('ModifyUserName') is not None:
            self.modify_user_name = m.get('ModifyUserName')

        if m.get('ProcessCanRetry') is not None:
            self.process_can_retry = m.get('ProcessCanRetry')

        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')

        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeDocResponseBodyDocTags(DaraModel):
    def __init__(
        self,
        default_tag: bool = None,
        group_id: int = None,
        group_name: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        self.default_tag = default_tag
        self.group_id = group_id
        self.group_name = group_name
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_tag is not None:
            result['DefaultTag'] = self.default_tag

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultTag') is not None:
            self.default_tag = m.get('DefaultTag')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class DescribeDocResponseBodyDocMetadata(DaraModel):
    def __init__(
        self,
        business_view_id: str = None,
        business_view_name: str = None,
        meta_cell_info_dtolist: List[main_models.DescribeDocResponseBodyDocMetadataMetaCellInfoDTOList] = None,
    ):
        self.business_view_id = business_view_id
        self.business_view_name = business_view_name
        self.meta_cell_info_dtolist = meta_cell_info_dtolist

    def validate(self):
        if self.meta_cell_info_dtolist:
            for v1 in self.meta_cell_info_dtolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_view_id is not None:
            result['BusinessViewId'] = self.business_view_id

        if self.business_view_name is not None:
            result['BusinessViewName'] = self.business_view_name

        result['MetaCellInfoDTOList'] = []
        if self.meta_cell_info_dtolist is not None:
            for k1 in self.meta_cell_info_dtolist:
                result['MetaCellInfoDTOList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessViewId') is not None:
            self.business_view_id = m.get('BusinessViewId')

        if m.get('BusinessViewName') is not None:
            self.business_view_name = m.get('BusinessViewName')

        self.meta_cell_info_dtolist = []
        if m.get('MetaCellInfoDTOList') is not None:
            for k1 in m.get('MetaCellInfoDTOList'):
                temp_model = main_models.DescribeDocResponseBodyDocMetadataMetaCellInfoDTOList()
                self.meta_cell_info_dtolist.append(temp_model.from_map(k1))

        return self

class DescribeDocResponseBodyDocMetadataMetaCellInfoDTOList(DaraModel):
    def __init__(
        self,
        field_code: str = None,
        field_name: str = None,
        value: str = None,
    ):
        self.field_code = field_code
        self.field_name = field_name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_code is not None:
            result['FieldCode'] = self.field_code

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldCode') is not None:
            self.field_code = m.get('FieldCode')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeDocResponseBodyDocInfo(DaraModel):
    def __init__(
        self,
        doc_paras: List[main_models.DescribeDocResponseBodyDocInfoDocParas] = None,
    ):
        self.doc_paras = doc_paras

    def validate(self):
        if self.doc_paras:
            for v1 in self.doc_paras:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DocParas'] = []
        if self.doc_paras is not None:
            for k1 in self.doc_paras:
                result['DocParas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.doc_paras = []
        if m.get('DocParas') is not None:
            for k1 in m.get('DocParas'):
                temp_model = main_models.DescribeDocResponseBodyDocInfoDocParas()
                self.doc_paras.append(temp_model.from_map(k1))

        return self

class DescribeDocResponseBodyDocInfoDocParas(DaraModel):
    def __init__(
        self,
        para_level: int = None,
        para_no: int = None,
        para_text: str = None,
        para_type: str = None,
    ):
        self.para_level = para_level
        self.para_no = para_no
        self.para_text = para_text
        self.para_type = para_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.para_level is not None:
            result['ParaLevel'] = self.para_level

        if self.para_no is not None:
            result['ParaNo'] = self.para_no

        if self.para_text is not None:
            result['ParaText'] = self.para_text

        if self.para_type is not None:
            result['ParaType'] = self.para_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParaLevel') is not None:
            self.para_level = m.get('ParaLevel')

        if m.get('ParaNo') is not None:
            self.para_no = m.get('ParaNo')

        if m.get('ParaText') is not None:
            self.para_text = m.get('ParaText')

        if m.get('ParaType') is not None:
            self.para_type = m.get('ParaType')

        return self

