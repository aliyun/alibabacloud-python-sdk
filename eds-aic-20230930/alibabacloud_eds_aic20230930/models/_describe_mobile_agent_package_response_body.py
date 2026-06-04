# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeMobileAgentPackageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        package_list: List[main_models.DescribeMobileAgentPackageResponseBodyPackageList] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.code = code
        self.message = message
        self.package_list = package_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.package_list:
            for v1 in self.package_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['PackageList'] = []
        if self.package_list is not None:
            for k1 in self.package_list:
                result['PackageList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.package_list = []
        if m.get('PackageList') is not None:
            for k1 in m.get('PackageList'):
                temp_model = main_models.DescribeMobileAgentPackageResponseBodyPackageList()
                self.package_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeMobileAgentPackageResponseBodyPackageList(DaraModel):
    def __init__(
        self,
        expired_at: str = None,
        instance_ids: List[str] = None,
        package_credit: str = None,
        package_id: str = None,
        package_spec: str = None,
        package_spec_name: str = None,
        package_status: str = None,
        used_credit: str = None,
    ):
        self.expired_at = expired_at
        self.instance_ids = instance_ids
        self.package_credit = package_credit
        self.package_id = package_id
        self.package_spec = package_spec
        self.package_spec_name = package_spec_name
        self.package_status = package_status
        self.used_credit = used_credit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_at is not None:
            result['ExpiredAt'] = self.expired_at

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.package_credit is not None:
            result['PackageCredit'] = self.package_credit

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.package_spec is not None:
            result['PackageSpec'] = self.package_spec

        if self.package_spec_name is not None:
            result['PackageSpecName'] = self.package_spec_name

        if self.package_status is not None:
            result['PackageStatus'] = self.package_status

        if self.used_credit is not None:
            result['UsedCredit'] = self.used_credit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredAt') is not None:
            self.expired_at = m.get('ExpiredAt')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PackageCredit') is not None:
            self.package_credit = m.get('PackageCredit')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('PackageSpec') is not None:
            self.package_spec = m.get('PackageSpec')

        if m.get('PackageSpecName') is not None:
            self.package_spec_name = m.get('PackageSpecName')

        if m.get('PackageStatus') is not None:
            self.package_status = m.get('PackageStatus')

        if m.get('UsedCredit') is not None:
            self.used_credit = m.get('UsedCredit')

        return self

