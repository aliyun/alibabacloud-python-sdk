# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class ListSharedTargetsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        shared_targets: List[main_models.ListSharedTargetsResponseBodySharedTargets] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information of the principals.
        self.shared_targets = shared_targets

    def validate(self):
        if self.shared_targets:
            for v1 in self.shared_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SharedTargets'] = []
        if self.shared_targets is not None:
            for k1 in self.shared_targets:
                result['SharedTargets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.shared_targets = []
        if m.get('SharedTargets') is not None:
            for k1 in m.get('SharedTargets'):
                temp_model = main_models.ListSharedTargetsResponseBodySharedTargets()
                self.shared_targets.append(temp_model.from_map(k1))

        return self

class ListSharedTargetsResponseBodySharedTargets(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        external: bool = None,
        resource_share_id: str = None,
        target_id: str = None,
        target_property: str = None,
        update_time: str = None,
    ):
        # The time when the principal was associated with the resource share.
        self.create_time = create_time
        # Indicates whether the principal is outside the resource directory. Valid values:
        # 
        # *   true
        # *   false
        self.external = external
        # The ID of the resource share.
        self.resource_share_id = resource_share_id
        # The ID of the principal or resource owner.
        # 
        # *   If the value of `ResourceOwner` is `Self`, the value of this parameter is the ID of a principal.
        # *   If the value of `ResourceOwner` is `OtherAccounts`, the value of this parameter is the ID of a resource owner.
        self.target_id = target_id
        # The properties of the principal, such as the time range within which the resource is shared.
        # 
        # >  This parameter is returned only if the principal is an Alibaba Cloud service.
        self.target_property = target_property
        # The time when the association of the principal was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.external is not None:
            result['External'] = self.external

        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_property is not None:
            result['TargetProperty'] = self.target_property

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('External') is not None:
            self.external = m.get('External')

        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetProperty') is not None:
            self.target_property = m.get('TargetProperty')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

