# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreatePrometheusInstanceRequest(DaraModel):
    def __init__(
        self,
        archive_duration: int = None,
        auth_free_read_policy: str = None,
        auth_free_write_policy: str = None,
        enable_auth_free_read: bool = None,
        enable_auth_free_write: bool = None,
        enable_auth_token: bool = None,
        payment_type: str = None,
        prometheus_instance_name: str = None,
        status: str = None,
        storage_duration: int = None,
        tags: List[main_models.CreatePrometheusInstanceRequestTags] = None,
        workspace: str = None,
    ):
        # The number of days that data is automatically archived after the storage duration expires. A value of 0 indicates that data is not archived. Valid values:
        # 
        # - V1 instances: 60 to 365.
        # 
        # - V2 instances: 60 to 3650. A value of 3650 indicates that the data is permanently stored.
        self.archive_duration = archive_duration
        # The policy for password-free read access. IP address ranges and VPC IDs are supported.
        self.auth_free_read_policy = auth_free_read_policy
        # The policy for password-free write access.
        self.auth_free_write_policy = auth_free_write_policy
        # Specifies whether to enable password-free read access. This feature is supported only for V2 instances.
        self.enable_auth_free_read = enable_auth_free_read
        # Specifies whether to enable password-free write access. This feature is supported only for V2 instances.
        self.enable_auth_free_write = enable_auth_free_write
        # Specifies whether to enable an authorization token. This feature is supported only for V1 instances.
        self.enable_auth_token = enable_auth_token
        # The billing method.
        # 
        # - POSTPAY: pay-as-you-go based on the volume of reported metrics.
        # 
        # - Note: If you leave this parameter empty, the default billing method is used. If a default billing method is not configured, POSTPAY is used.
        self.payment_type = payment_type
        # The name of the instance.
        # 
        # This parameter is required.
        self.prometheus_instance_name = prometheus_instance_name
        # The instance status.
        self.status = status
        # The storage duration of the instance in days. The valid values depend on the billing method:
        # 
        # - For instances billed based on data written: 90 and 180.
        # 
        # - For instances billed based on reported metrics: 15, 30, 60, 90, and 180.
        self.storage_duration = storage_duration
        # The tags.
        self.tags = tags
        # The workspace to which the instance belongs. The default value is default-cms-{userId}-{regionId}.
        self.workspace = workspace

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

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

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

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

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreatePrometheusInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class CreatePrometheusInstanceRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

