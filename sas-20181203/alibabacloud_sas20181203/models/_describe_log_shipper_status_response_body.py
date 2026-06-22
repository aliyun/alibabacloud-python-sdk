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
        # The log delivery status collection.
        self.log_shipper_status = log_shipper_status
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
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
        # The service authorization status of the log analysis feature. Valid values:
        # 
        # - **yes**: authorized
        # - **no**: not authorized.
        self.auth_status = auth_status
        # The purchase status of the log analysis feature. Valid values:
        # 
        # - **yes**: purchased
        # - **no**: not purchased.
        self.buy_status = buy_status
        # The version of the log delivery fields for log analysis. Valid values:
        # 
        # - **SAS_V1**
        # - **SAS_V2**.
        self.etl_meta_version = etl_meta_version
        # The enabling status of log analysis. Valid values:
        # 
        # - **yes**: enabled
        # - **no**: not enabled.
        self.open_status = open_status
        # The pay-as-you-go activation status of the log analysis feature. Valid values:
        # 
        # - **yes**: activated
        # - **no**: not activated.
        self.post_paid_open_status = post_paid_open_status
        # The pay-as-you-go support status of the log analysis feature. Valid values:
        # 
        # - **yes**: supported
        # - **no**: not supported.
        self.post_paid_support_status = post_paid_support_status
        # The status of the log project used by the log analysis feature. Valid values:
        # 
        # - **Normal**: Normal.
        # - **Disable**: Disabled.
        self.sls_project_status = sls_project_status
        # The activation status of Simple Log Service (SLS). Valid values:
        # 
        # - **yes**: activated
        # - **no**: not activated.
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

