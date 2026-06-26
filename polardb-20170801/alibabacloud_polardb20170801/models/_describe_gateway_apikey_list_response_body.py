# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeGatewayApikeyListResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeGatewayApikeyListResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        total_pages: int = None,
        total_record_count: int = None,
    ):
        # The list of consumer objects.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of records on the current page.
        self.page_record_count = page_record_count
        # The number of entries per page. Valid values:
        # * **30**
        # * **50**
        # * **100**
        # 
        # Default value: 30.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The total number of pages.
        self.total_pages = total_pages
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeGatewayApikeyListResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeGatewayApikeyListResponseBodyItems(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        consumer_group_id: str = None,
        consumer_id: str = None,
        consumer_tag: str = None,
        create_time: str = None,
        gw_cluster_id: str = None,
        modify_time: str = None,
        name: str = None,
    ):
        # The API key in use.
        self.api_key = api_key
        # The user group ID.
        self.consumer_group_id = consumer_group_id
        # The user ID.
        self.consumer_id = consumer_id
        # The consumer tag.
        self.consumer_tag = consumer_tag
        # The creation time.
        self.create_time = create_time
        # The gateway instance ID.
        self.gw_cluster_id = gw_cluster_id
        # The last modification time.
        self.modify_time = modify_time
        # The username.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id

        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.consumer_tag is not None:
            result['ConsumerTag'] = self.consumer_tag

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('ConsumerTag') is not None:
            self.consumer_tag = m.get('ConsumerTag')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

