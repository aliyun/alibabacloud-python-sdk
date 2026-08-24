# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListProhibitedSoftwareShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        device_type: str = None,
        name: str = None,
        page_size: int = None,
        policy_id: str = None,
        process_name: str = None,
        software_ids: List[main_models.ListProhibitedSoftwareShrinkRequestSoftwareIds] = None,
        tag_id_shrink: str = None,
    ):
        # The page number of the current page in a paged query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The operating system type for which the prohibited software has configured processes.
        self.device_type = device_type
        # The name of the prohibited software.
        self.name = name
        # The number of entries per page in a paged query. Valid values: 1 to 500.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the software prohibition policy. You can obtain the value from the following operations:
        # - [ListProhibitedPolicies](~~ListProhibitedPolicies~~): Lists software prohibition policies.
        # - [CreateProhibitedPolicy](~~CreateProhibitedPolicy~~): Creates a software prohibition policy.
        self.policy_id = policy_id
        # The process name.
        self.process_name = process_name
        # The collection of prohibited software IDs. Duplicate values are not allowed.
        self.software_ids = software_ids
        # The unique identifier of the prohibited software tag.
        self.tag_id_shrink = tag_id_shrink

    def validate(self):
        if self.software_ids:
            for v1 in self.software_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        result['SoftwareIds'] = []
        if self.software_ids is not None:
            for k1 in self.software_ids:
                result['SoftwareIds'].append(k1.to_map() if k1 else None)

        if self.tag_id_shrink is not None:
            result['TagId'] = self.tag_id_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        self.software_ids = []
        if m.get('SoftwareIds') is not None:
            for k1 in m.get('SoftwareIds'):
                temp_model = main_models.ListProhibitedSoftwareShrinkRequestSoftwareIds()
                self.software_ids.append(temp_model.from_map(k1))

        if m.get('TagId') is not None:
            self.tag_id_shrink = m.get('TagId')

        return self

class ListProhibitedSoftwareShrinkRequestSoftwareIds(DaraModel):
    def __init__(
        self,
        is_default: bool = None,
        software_id: str = None,
    ):
        # Indicates whether the prohibited software is a system built-in prohibited software. Valid values:
        # - **true**: A system built-in prohibited software that is shared across all Alibaba Cloud accounts and cannot be modified or deleted.
        # - **false**: Custom prohibited software under the current Alibaba Cloud account.
        self.is_default = is_default
        # The ID of the prohibited software. You can obtain the value from the following operations:
        # - [ListProhibitedSoftware](~~ListProhibitedSoftware~~): Lists prohibited software.
        # - [CreateProhibitedSoftware](~~CreateProhibitedSoftware~~): Creates custom prohibited software.
        self.software_id = software_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.software_id is not None:
            result['SoftwareId'] = self.software_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')

        return self

