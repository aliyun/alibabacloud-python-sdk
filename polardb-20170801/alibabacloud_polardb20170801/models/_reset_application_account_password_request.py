# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetApplicationAccountPasswordRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        application_id: str = None,
        new_account_password: str = None,
    ):
        # The account name.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The application ID. Only applications associated with PolarDB for MySQL clusters are accepted. Before the call, you can obtain the DBClusterId associated with the application by calling DescribeApplicationAttribute, and then query the DBType of the cluster by calling DescribeDBClusterAttribute to confirm that the value is MySQL. Associated applications of other engine types are not applicable.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The new password.
        # 
        # This parameter is required.
        self.new_account_password = new_account_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.new_account_password is not None:
            result['NewAccountPassword'] = self.new_account_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('NewAccountPassword') is not None:
            self.new_account_password = m.get('NewAccountPassword')

        return self

