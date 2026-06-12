# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceSharedAccountsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        share_account: List[main_models.ListServiceSharedAccountsResponseBodyShareAccount] = None,
        total_count: int = None,
    ):
        # The number of entries returned on each page. Maximum value: 100. Default value: 20.
        self.max_results = max_results
        # The token used to start the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about the shared accounts.
        self.share_account = share_account
        # The total number of entries that meet the filter criteria.
        self.total_count = total_count

    def validate(self):
        if self.share_account:
            for v1 in self.share_account:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ShareAccount'] = []
        if self.share_account is not None:
            for k1 in self.share_account:
                result['ShareAccount'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.share_account = []
        if m.get('ShareAccount') is not None:
            for k1 in m.get('ShareAccount'):
                temp_model = main_models.ListServiceSharedAccountsResponseBodyShareAccount()
                self.share_account.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServiceSharedAccountsResponseBodyShareAccount(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        logo: str = None,
        name: str = None,
        permission: str = None,
        service_id: str = None,
        update_time: str = None,
        user_ali_uid: str = None,
    ):
        # The time when the sharing was created.
        self.create_time = create_time
        # The logo of the distributor.
        self.logo = logo
        # The name of the distributor.
        self.name = name
        # The permission type. Valid values:
        # 
        # - Deployable: The service is deployable.
        # 
        # - Accessible: The service is accessible.
        self.permission = permission
        # The service ID.
        self.service_id = service_id
        # The time when the sharing was last updated.
        self.update_time = update_time
        # The Alibaba Cloud account ID of the user.
        self.user_ali_uid = user_ali_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.logo is not None:
            result['Logo'] = self.logo

        if self.name is not None:
            result['Name'] = self.name

        if self.permission is not None:
            result['Permission'] = self.permission

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Logo') is not None:
            self.logo = m.get('Logo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Permission') is not None:
            self.permission = m.get('Permission')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')

        return self

