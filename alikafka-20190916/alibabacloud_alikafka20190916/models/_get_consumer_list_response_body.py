# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetConsumerListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        consumer_list: main_models.GetConsumerListResponseBodyConsumerList = None,
        current_page: int = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        # The HTTP status code returned. The HTTP status code 200 indicates that the request is successful.
        self.code = code
        self.consumer_list = consumer_list
        # The number of the page to return. Pages start from page 1.
        self.current_page = current_page
        # The returned message.
        self.message = message
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.consumer_list:
            self.consumer_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.consumer_list is not None:
            result['ConsumerList'] = self.consumer_list.to_map()

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConsumerList') is not None:
            temp_model = main_models.GetConsumerListResponseBodyConsumerList()
            self.consumer_list = temp_model.from_map(m.get('ConsumerList'))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetConsumerListResponseBodyConsumerList(DaraModel):
    def __init__(
        self,
        consumer_vo: List[main_models.GetConsumerListResponseBodyConsumerListConsumerVO] = None,
    ):
        self.consumer_vo = consumer_vo

    def validate(self):
        if self.consumer_vo:
            for v1 in self.consumer_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConsumerVO'] = []
        if self.consumer_vo is not None:
            for k1 in self.consumer_vo:
                result['ConsumerVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumer_vo = []
        if m.get('ConsumerVO') is not None:
            for k1 in m.get('ConsumerVO'):
                temp_model = main_models.GetConsumerListResponseBodyConsumerListConsumerVO()
                self.consumer_vo.append(temp_model.from_map(k1))

        return self

class GetConsumerListResponseBodyConsumerListConsumerVO(DaraModel):
    def __init__(
        self,
        automatically_created_group: bool = None,
        consumer_id: str = None,
        create_time: int = None,
        instance_id: str = None,
        region_id: str = None,
        remark: str = None,
        tags: main_models.GetConsumerListResponseBodyConsumerListConsumerVOTags = None,
    ):
        self.automatically_created_group = automatically_created_group
        self.consumer_id = consumer_id
        self.create_time = create_time
        self.instance_id = instance_id
        self.region_id = region_id
        self.remark = remark
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.automatically_created_group is not None:
            result['AutomaticallyCreatedGroup'] = self.automatically_created_group

        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutomaticallyCreatedGroup') is not None:
            self.automatically_created_group = m.get('AutomaticallyCreatedGroup')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Tags') is not None:
            temp_model = main_models.GetConsumerListResponseBodyConsumerListConsumerVOTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class GetConsumerListResponseBodyConsumerListConsumerVOTags(DaraModel):
    def __init__(
        self,
        tag_vo: List[main_models.GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO] = None,
    ):
        self.tag_vo = tag_vo

    def validate(self):
        if self.tag_vo:
            for v1 in self.tag_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagVO'] = []
        if self.tag_vo is not None:
            for k1 in self.tag_vo:
                result['TagVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_vo = []
        if m.get('TagVO') is not None:
            for k1 in m.get('TagVO'):
                temp_model = main_models.GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO()
                self.tag_vo.append(temp_model.from_map(k1))

        return self

class GetConsumerListResponseBodyConsumerListConsumerVOTagsTagVO(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

