# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class UpdatePrometheusInstanceRequest(DaraModel):
    def __init__(
        self,
        archive_duration: int = None,
        auth_free_read_policy: str = None,
        auth_free_write_policy: str = None,
        dryrun: bool = None,
        enable_auth_free_read: bool = None,
        enable_auth_free_write: bool = None,
        enable_auth_token: bool = None,
        payment_type: str = None,
        prometheus_instance_name: str = None,
        status: str = None,
        storage_duration: int = None,
        store_config: main_models.PrometheusInstanceStoreConfig = None,
        workspace: str = None,
    ):
        # The number of days to automatically archive and retain data after the storage period expires. A value of 0 indicates that data is not archived. Valid values for the archive retention period:
        # V1: 1 to 365 days. Supported only for the pay-by-ingested-data billing method.
        # V2: 1 to 3650 days. A value of 3650 indicates permanent retention.
        self.archive_duration = archive_duration
        # The authentication-free read policy. IP address ranges and VPC IDs are supported.
        self.auth_free_read_policy = auth_free_read_policy
        # The authentication-free read policy. IP address ranges and VPC IDs are supported.
        self.auth_free_write_policy = auth_free_write_policy
        # Specifies whether to only precheck the request. Valid values:
        # 
        # true: sends a precheck request without updating the instance. The system checks whether required parameters are specified, the request format is valid, and service limits are met. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the DryRunOperation error code is returned.
        # false: sends a regular request. If the request passes the precheck, the instance is updated. This is the default value.
        self.dryrun = dryrun
        # Specifies whether to enable authentication-free read.
        self.enable_auth_free_read = enable_auth_free_read
        # Specifies whether to enable authentication-free write.
        self.enable_auth_free_write = enable_auth_free_write
        # Specifies whether to enable access token authentication.
        self.enable_auth_token = enable_auth_token
        # The billing method. You can change the billing method only once during the lifecycle of the instance. Valid values:
        # POSTPAY: pay-as-you-go based on the number of reported metrics.
        # POSTPAY_GB: pay-as-you-go based on the volume of ingested data.
        self.payment_type = payment_type
        # The name of the instance.
        self.prometheus_instance_name = prometheus_instance_name
        # The status of the instance storage database. Only RUNNING is supported. If this parameter is left empty, the status of the storage database is not changed.
        self.status = status
        # The storage duration in days. Valid values:
        # For the pay-by-ingested-data billing method: 90 and 180.
        # For the pay-by-reported-metrics billing method: 15, 30, 60, 90, and 180.
        self.storage_duration = storage_duration
        # The Prometheus storage configuration.
        self.store_config = store_config
        # The workspace to which the instance belongs.
        self.workspace = workspace

    def validate(self):
        if self.store_config:
            self.store_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_duration is not None:
            result['archiveDuration'] = self.archive_duration

        if self.auth_free_read_policy is not None:
            result['authFreeReadPolicy'] = self.auth_free_read_policy

        if self.auth_free_write_policy is not None:
            result['authFreeWritePolicy'] = self.auth_free_write_policy

        if self.dryrun is not None:
            result['dryrun'] = self.dryrun

        if self.enable_auth_free_read is not None:
            result['enableAuthFreeRead'] = self.enable_auth_free_read

        if self.enable_auth_free_write is not None:
            result['enableAuthFreeWrite'] = self.enable_auth_free_write

        if self.enable_auth_token is not None:
            result['enableAuthToken'] = self.enable_auth_token

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.prometheus_instance_name is not None:
            result['prometheusInstanceName'] = self.prometheus_instance_name

        if self.status is not None:
            result['status'] = self.status

        if self.storage_duration is not None:
            result['storageDuration'] = self.storage_duration

        if self.store_config is not None:
            result['storeConfig'] = self.store_config.to_map()

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('archiveDuration') is not None:
            self.archive_duration = m.get('archiveDuration')

        if m.get('authFreeReadPolicy') is not None:
            self.auth_free_read_policy = m.get('authFreeReadPolicy')

        if m.get('authFreeWritePolicy') is not None:
            self.auth_free_write_policy = m.get('authFreeWritePolicy')

        if m.get('dryrun') is not None:
            self.dryrun = m.get('dryrun')

        if m.get('enableAuthFreeRead') is not None:
            self.enable_auth_free_read = m.get('enableAuthFreeRead')

        if m.get('enableAuthFreeWrite') is not None:
            self.enable_auth_free_write = m.get('enableAuthFreeWrite')

        if m.get('enableAuthToken') is not None:
            self.enable_auth_token = m.get('enableAuthToken')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('prometheusInstanceName') is not None:
            self.prometheus_instance_name = m.get('prometheusInstanceName')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('storageDuration') is not None:
            self.storage_duration = m.get('storageDuration')

        if m.get('storeConfig') is not None:
            temp_model = main_models.PrometheusInstanceStoreConfig()
            self.store_config = temp_model.from_map(m.get('storeConfig'))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

