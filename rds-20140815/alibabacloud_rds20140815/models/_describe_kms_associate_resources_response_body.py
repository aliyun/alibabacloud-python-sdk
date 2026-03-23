# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeKmsAssociateResourcesResponseBody(DaraModel):
    def __init__(
        self,
        associate_dbinstances: List[main_models.DescribeKmsAssociateResourcesResponseBodyAssociateDBInstances] = None,
        associate_status: bool = None,
        request_id: str = None,
    ):
        self.associate_dbinstances = associate_dbinstances
        self.associate_status = associate_status
        self.request_id = request_id

    def validate(self):
        if self.associate_dbinstances:
            for v1 in self.associate_dbinstances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssociateDBInstances'] = []
        if self.associate_dbinstances is not None:
            for k1 in self.associate_dbinstances:
                result['AssociateDBInstances'].append(k1.to_map() if k1 else None)

        if self.associate_status is not None:
            result['AssociateStatus'] = self.associate_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associate_dbinstances = []
        if m.get('AssociateDBInstances') is not None:
            for k1 in m.get('AssociateDBInstances'):
                temp_model = main_models.DescribeKmsAssociateResourcesResponseBodyAssociateDBInstances()
                self.associate_dbinstances.append(temp_model.from_map(k1))

        if m.get('AssociateStatus') is not None:
            self.associate_status = m.get('AssociateStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeKmsAssociateResourcesResponseBodyAssociateDBInstances(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        engine: str = None,
        key_used_by: str = None,
        status: str = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.engine = engine
        self.key_used_by = key_used_by
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.key_used_by is not None:
            result['KeyUsedBy'] = self.key_used_by

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('KeyUsedBy') is not None:
            self.key_used_by = m.get('KeyUsedBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

