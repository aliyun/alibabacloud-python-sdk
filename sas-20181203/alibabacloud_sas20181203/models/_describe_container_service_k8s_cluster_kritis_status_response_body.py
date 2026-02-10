# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeContainerServiceK8sClusterKritisStatusResponseBody(DaraModel):
    def __init__(
        self,
        kritis_status: main_models.DescribeContainerServiceK8sClusterKritisStatusResponseBodyKritisStatus = None,
        request_id: str = None,
    ):
        # The Kritis status of the ACK cluster.
        self.kritis_status = kritis_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.kritis_status:
            self.kritis_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kritis_status is not None:
            result['KritisStatus'] = self.kritis_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KritisStatus') is not None:
            temp_model = main_models.DescribeContainerServiceK8sClusterKritisStatusResponseBodyKritisStatus()
            self.kritis_status = temp_model.from_map(m.get('KritisStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContainerServiceK8sClusterKritisStatusResponseBodyKritisStatus(DaraModel):
    def __init__(
        self,
        install: bool = None,
    ):
        # Indicates whether Kritis is installed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.install = install

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.install is not None:
            result['Install'] = self.install

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Install') is not None:
            self.install = m.get('Install')

        return self

