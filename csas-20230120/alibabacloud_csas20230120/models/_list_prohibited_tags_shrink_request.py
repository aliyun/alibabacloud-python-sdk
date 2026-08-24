# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListProhibitedTagsShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        policy_id: str = None,
        software_id_shrink: str = None,
        tag_ids: List[main_models.ListProhibitedTagsShrinkRequestTagIds] = None,
    ):
        # The page number of the current page in a paged query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The name of the prohibited software tag. Fuzzy match is supported. The name can be up to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        self.name = name
        # The number of entries per page in a paged query. Valid values: 1 to 500.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the software prohibition policy. You can obtain the value from the following operations:
        # - [ListProhibitedPolicies](~~ListProhibitedPolicies~~): Lists software prohibition policies.
        # - [CreateProhibitedPolicy](~~CreateProhibitedPolicy~~): Creates a software prohibition policy.
        self.policy_id = policy_id
        # The unique identifier of the prohibited software.
        self.software_id_shrink = software_id_shrink
        # The collection of prohibited software tag IDs. Duplicate values are not allowed. A maximum of 500 IDs can be specified.
        self.tag_ids = tag_ids

    def validate(self):
        if self.tag_ids:
            for v1 in self.tag_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.software_id_shrink is not None:
            result['SoftwareId'] = self.software_id_shrink

        result['TagIds'] = []
        if self.tag_ids is not None:
            for k1 in self.tag_ids:
                result['TagIds'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('SoftwareId') is not None:
            self.software_id_shrink = m.get('SoftwareId')

        self.tag_ids = []
        if m.get('TagIds') is not None:
            for k1 in m.get('TagIds'):
                temp_model = main_models.ListProhibitedTagsShrinkRequestTagIds()
                self.tag_ids.append(temp_model.from_map(k1))

        return self

class ListProhibitedTagsShrinkRequestTagIds(DaraModel):
    def __init__(
        self,
        is_default: bool = None,
        tag_id: str = None,
    ):
        # Indicates whether the prohibited software tag is a system built-in tag. Valid values:
        # - **true**: A system built-in tag that is shared across all Alibaba Cloud accounts and cannot be modified or deleted.
        # - **false**: A custom tag under the current Alibaba Cloud account.
        self.is_default = is_default
        # The ID of the prohibited software tag. You can obtain the value from the following operations:
        # - [ListProhibitedTags](~~ListProhibitedTags~~): Lists prohibited software tags.
        # - [CreateProhibitedTag](~~CreateProhibitedTag~~): Creates a custom prohibited software tag.
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

