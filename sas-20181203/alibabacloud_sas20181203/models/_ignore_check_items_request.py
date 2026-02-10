# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class IgnoreCheckItemsRequest(DaraModel):
    def __init__(
        self,
        check_and_risk_type_list: List[main_models.IgnoreCheckItemsRequestCheckAndRiskTypeList] = None,
        check_ids: List[int] = None,
        container_items: List[main_models.IgnoreCheckItemsRequestContainerItems] = None,
        lang: str = None,
        reason: str = None,
        source: str = None,
        type: int = None,
        uuid_list: List[str] = None,
    ):
        # The information about check items.
        self.check_and_risk_type_list = check_and_risk_type_list
        # The IDs of check items.
        self.check_ids = check_ids
        # List of container names that need to be whitelisted.
        self.container_items = container_items
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The reason why you add the risk item to the whitelist.
        self.reason = reason
        # The data source. Valid values:
        # 
        # *   **default**: host baseline
        # *   **agentless**: agentless baseline
        self.source = source
        # The operation that you want to perform on the risk item.Valid values:
        # *  **1**: adds the risk item to the whitelist
        # *  **2**: removes the risk item from the whitelist
        # 
        # This parameter is required.
        self.type = type
        # The UUIDs of the servers.
        # 
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        self.uuid_list = uuid_list

    def validate(self):
        if self.check_and_risk_type_list:
            for v1 in self.check_and_risk_type_list:
                 if v1:
                    v1.validate()
        if self.container_items:
            for v1 in self.container_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckAndRiskTypeList'] = []
        if self.check_and_risk_type_list is not None:
            for k1 in self.check_and_risk_type_list:
                result['CheckAndRiskTypeList'].append(k1.to_map() if k1 else None)

        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        result['ContainerItems'] = []
        if self.container_items is not None:
            for k1 in self.container_items:
                result['ContainerItems'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.source is not None:
            result['Source'] = self.source

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_and_risk_type_list = []
        if m.get('CheckAndRiskTypeList') is not None:
            for k1 in m.get('CheckAndRiskTypeList'):
                temp_model = main_models.IgnoreCheckItemsRequestCheckAndRiskTypeList()
                self.check_and_risk_type_list.append(temp_model.from_map(k1))

        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        self.container_items = []
        if m.get('ContainerItems') is not None:
            for k1 in m.get('ContainerItems'):
                temp_model = main_models.IgnoreCheckItemsRequestContainerItems()
                self.container_items.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

class IgnoreCheckItemsRequestContainerItems(DaraModel):
    def __init__(
        self,
        container_names: str = None,
        uuid: str = None,
    ):
        # The names of the containers that need to be whitelisted for the current asset, separated by English commas.
        self.container_names = container_names
        # The UUID of the server.
        # 
        # > You can call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/141932.html) operation to query the UUIDs of servers.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_names is not None:
            result['ContainerNames'] = self.container_names

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerNames') is not None:
            self.container_names = m.get('ContainerNames')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class IgnoreCheckItemsRequestCheckAndRiskTypeList(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        risk_type: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The baseline type of the check item.
        self.risk_type = risk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        return self

