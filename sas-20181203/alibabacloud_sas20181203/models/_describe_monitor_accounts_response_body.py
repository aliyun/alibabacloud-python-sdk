# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitorAccountsResponseBody(DaraModel):
    def __init__(
        self,
        account_id_infos: List[main_models.DescribeMonitorAccountsResponseBodyAccountIdInfos] = None,
        account_ids: List[str] = None,
        request_id: str = None,
    ):
        # List of member account information.
        self.account_id_infos = account_id_infos
        # The IDs of the members.
        self.account_ids = account_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.account_id_infos:
            for v1 in self.account_id_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountIdInfos'] = []
        if self.account_id_infos is not None:
            for k1 in self.account_id_infos:
                result['AccountIdInfos'].append(k1.to_map() if k1 else None)

        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_id_infos = []
        if m.get('AccountIdInfos') is not None:
            for k1 in m.get('AccountIdInfos'):
                temp_model = main_models.DescribeMonitorAccountsResponseBodyAccountIdInfos()
                self.account_id_infos.append(temp_model.from_map(k1))

        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMonitorAccountsResponseBodyAccountIdInfos(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        add_time: int = None,
        operator_uid: str = None,
        post_basic_service: int = None,
        sas_version: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The time when it was added to the control list, in timestamp format with second precision.
        self.add_time = add_time
        # The account ID of the operator.
        self.operator_uid = operator_uid
        # Basic service switch. Values: 
        # - **0**: Off 
        # - **1**: On
        self.post_basic_service = post_basic_service
        # The purchased version of Cloud Security Center. Values:
        # - **0** or **1**: Free Edition 
        # - **2** or **3**: Enterprise Edition
        #  - **5**: Advanced Edition 
        # - **6**: Anti-Virus Edition 
        # - **7**: Flagship Edition
        self.sas_version = sas_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.add_time is not None:
            result['AddTime'] = self.add_time

        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid

        if self.post_basic_service is not None:
            result['PostBasicService'] = self.post_basic_service

        if self.sas_version is not None:
            result['SasVersion'] = self.sas_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')

        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')

        if m.get('PostBasicService') is not None:
            self.post_basic_service = m.get('PostBasicService')

        if m.get('SasVersion') is not None:
            self.sas_version = m.get('SasVersion')

        return self

