# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListLiveTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.ListLiveTagResourcesRequestTag] = None,
        tag_owner_bid: str = None,
        tag_owner_uid: str = None,
    ):
        self.next_token = next_token
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.tag = tag
        self.tag_owner_bid = tag_owner_bid
        self.tag_owner_uid = tag_owner_uid

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
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tag_owner_bid is not None:
            result['TagOwnerBid'] = self.tag_owner_bid

        if self.tag_owner_uid is not None:
            result['TagOwnerUid'] = self.tag_owner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListLiveTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TagOwnerBid') is not None:
            self.tag_owner_bid = m.get('TagOwnerBid')

        if m.get('TagOwnerUid') is not None:
            self.tag_owner_uid = m.get('TagOwnerUid')

        return self

class ListLiveTagResourcesRequestTag(DaraModel):
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

