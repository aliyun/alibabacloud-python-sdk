# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListEndpointGroupsRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        access_log_switch: str = None,
        endpoint_group_id: str = None,
        endpoint_group_type: str = None,
        listener_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        tag: List[main_models.ListEndpointGroupsRequestTag] = None,
    ):
        # The ID of the GA instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # Specifies whether the access logging feature is enabled. Default value: off. Valid values:
        # 
        # *   **on**: The access logging feature is enabled.
        # *   **off**: The access logging feature is disabled.
        self.access_log_switch = access_log_switch
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # The type of the endpoint group. Valid values: Valid values:
        # 
        # *   **default**
        # *   **virtual**
        # *   If you leave this parameter empty, all default and virtual endpoint groups are queried.
        self.endpoint_group_type = endpoint_group_type
        # The ID of the listener.
        self.listener_id = listener_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The tag of the endpoint group.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListEndpointGroupsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListEndpointGroupsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the endpoint group. It cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        # 
        # You can specify up to 20 tag keys.
        self.key = key
        # The tag value of the endpoint group. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `aliyun` or `acs:`.
        # 
        # You can specify up to 20 tag values.
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

