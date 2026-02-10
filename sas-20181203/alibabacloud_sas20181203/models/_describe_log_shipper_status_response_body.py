# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeLogShipperStatusResponseBody(DaraModel):
    def __init__(
        self,
        log_shipper_status: main_models.DescribeLogShipperStatusResponseBodyLogShipperStatus = None,
        request_id: str = None,
    ):
        # The status information.
        self.log_shipper_status = log_shipper_status
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.log_shipper_status:
            self.log_shipper_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_shipper_status is not None:
            result['LogShipperStatus'] = self.log_shipper_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogShipperStatus') is not None:
            temp_model = main_models.DescribeLogShipperStatusResponseBodyLogShipperStatus()
            self.log_shipper_status = temp_model.from_map(m.get('LogShipperStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLogShipperStatusResponseBodyLogShipperStatus(DaraModel):
    def __init__(
        self,
        auth_status: str = None,
        buy_status: str = None,
        etl_meta_version: str = None,
        open_status: str = None,
        post_paid_open_status: str = None,
        post_paid_support_status: str = None,
        sls_project_status: str = None,
        sls_service_status: str = None,
    ):
        # Indicates whether Security Center is authorized to access Log Service. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.auth_status = auth_status
        # Indicates whether the log analysis feature is purchased. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.buy_status = buy_status
        # The version of the log analysis field. Valid values:
        # - SAS_V1
        # - SAS_V2
        self.etl_meta_version = etl_meta_version
        # The status of the log analysis feature. Valid values:
        # 
        # *   **yes**: enabled
        # *   **no**: disabled
        self.open_status = open_status
        # Indicates whether the pay-as-you-go billing method is used. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.post_paid_open_status = post_paid_open_status
        # Indicates whether the log analysis feature supports the pay-as-you-go billing method. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.post_paid_support_status = post_paid_support_status
        # The status of the dedicated Log Service project. Valid values:
        # 
        # *   **Normal**: normal
        # *   **Disable**: disabled
        self.sls_project_status = sls_project_status
        # Indicates whether Log Service is activated. Valid values:
        # 
        # *   **yes**
        # *   **no**
        self.sls_service_status = sls_service_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status

        if self.buy_status is not None:
            result['BuyStatus'] = self.buy_status

        if self.etl_meta_version is not None:
            result['EtlMetaVersion'] = self.etl_meta_version

        if self.open_status is not None:
            result['OpenStatus'] = self.open_status

        if self.post_paid_open_status is not None:
            result['PostPaidOpenStatus'] = self.post_paid_open_status

        if self.post_paid_support_status is not None:
            result['PostPaidSupportStatus'] = self.post_paid_support_status

        if self.sls_project_status is not None:
            result['SlsProjectStatus'] = self.sls_project_status

        if self.sls_service_status is not None:
            result['SlsServiceStatus'] = self.sls_service_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')

        if m.get('BuyStatus') is not None:
            self.buy_status = m.get('BuyStatus')

        if m.get('EtlMetaVersion') is not None:
            self.etl_meta_version = m.get('EtlMetaVersion')

        if m.get('OpenStatus') is not None:
            self.open_status = m.get('OpenStatus')

        if m.get('PostPaidOpenStatus') is not None:
            self.post_paid_open_status = m.get('PostPaidOpenStatus')

        if m.get('PostPaidSupportStatus') is not None:
            self.post_paid_support_status = m.get('PostPaidSupportStatus')

        if m.get('SlsProjectStatus') is not None:
            self.sls_project_status = m.get('SlsProjectStatus')

        if m.get('SlsServiceStatus') is not None:
            self.sls_service_status = m.get('SlsServiceStatus')

        return self

