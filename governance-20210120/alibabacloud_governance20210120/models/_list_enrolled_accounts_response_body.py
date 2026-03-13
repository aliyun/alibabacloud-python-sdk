# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class ListEnrolledAccountsResponseBody(DaraModel):
    def __init__(
        self,
        enrolled_accounts: List[main_models.ListEnrolledAccountsResponseBodyEnrolledAccounts] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The enrolled accounts.
        self.enrolled_accounts = enrolled_accounts
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.enrolled_accounts:
            for v1 in self.enrolled_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnrolledAccounts'] = []
        if self.enrolled_accounts is not None:
            for k1 in self.enrolled_accounts:
                result['EnrolledAccounts'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.enrolled_accounts = []
        if m.get('EnrolledAccounts') is not None:
            for k1 in m.get('EnrolledAccounts'):
                temp_model = main_models.ListEnrolledAccountsResponseBodyEnrolledAccounts()
                self.enrolled_accounts.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEnrolledAccountsResponseBodyEnrolledAccounts(DaraModel):
    def __init__(
        self,
        account_uid: int = None,
        baseline_id: str = None,
        create_time: str = None,
        display_name: str = None,
        folder_id: str = None,
        payer_account_uid: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # The account ID.
        self.account_uid = account_uid
        # The ID of the baseline that is implemented.
        self.baseline_id = baseline_id
        # The creation time.
        self.create_time = create_time
        # The display name of the account.
        self.display_name = display_name
        # The ID of the parent folder.
        self.folder_id = folder_id
        # The ID of the settlement account.
        self.payer_account_uid = payer_account_uid
        # The creation status. Valid values:
        # 
        # *   Pending: The account is pending to be created.
        # *   Running: The account is being created.
        # *   Finished: The account is created.
        # *   Failed: The account fails to be created.
        # *   Scheduling: The account is being scheduled.
        # *   ScheduleFailed: The account fails to be scheduled.
        self.status = status
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid

        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.payer_account_uid is not None:
            result['PayerAccountUid'] = self.payer_account_uid

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')

        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('PayerAccountUid') is not None:
            self.payer_account_uid = m.get('PayerAccountUid')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

