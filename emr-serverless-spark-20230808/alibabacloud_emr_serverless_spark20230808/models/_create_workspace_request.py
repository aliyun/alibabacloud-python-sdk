# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class CreateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        auto_renew: str = None,
        auto_renew_period: str = None,
        auto_renew_period_unit: str = None,
        auto_start_session_cluster: bool = None,
        client_token: str = None,
        dlf_catalog_id: str = None,
        dlf_type: str = None,
        duration: str = None,
        oss_bucket: str = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        ram_role_name: str = None,
        release_type: str = None,
        resource_spec: main_models.CreateWorkspaceRequestResourceSpec = None,
        tag: List[main_models.CreateWorkspaceRequestTag] = None,
        workspace_name: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable auto-renewal. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew = auto_renew
        # The auto-renewal duration. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew_period = auto_renew_period
        # The unit of the auto-renewal duration. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew_period_unit = auto_renew_period_unit
        # Specifies whether to automatically start a session.
        self.auto_start_session_cluster = auto_start_session_cluster
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The information of the Data Lake Formation (DLF) catalog.
        self.dlf_catalog_id = dlf_catalog_id
        # The version of DLF.
        self.dlf_type = dlf_type
        # The subscription period. This parameter is required only if the paymentType parameter is set to Pre.
        self.duration = duration
        # The name of the Object Storage Service (OSS) bucket.
        self.oss_bucket = oss_bucket
        # The unit of the subscription duration.
        self.payment_duration_unit = payment_duration_unit
        # The billing method. Valid values:
        # 
        # *   PayAsYouGo
        # *   Pre
        self.payment_type = payment_type
        # The name of the role used to run Spark jobs.
        self.ram_role_name = ram_role_name
        # The type of the version.
        self.release_type = release_type
        # The resource specifications.
        self.resource_spec = resource_spec
        self.tag = tag
        # The name of the workspace.
        self.workspace_name = workspace_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period

        if self.auto_renew_period_unit is not None:
            result['autoRenewPeriodUnit'] = self.auto_renew_period_unit

        if self.auto_start_session_cluster is not None:
            result['autoStartSessionCluster'] = self.auto_start_session_cluster

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.dlf_catalog_id is not None:
            result['dlfCatalogId'] = self.dlf_catalog_id

        if self.dlf_type is not None:
            result['dlfType'] = self.dlf_type

        if self.duration is not None:
            result['duration'] = self.duration

        if self.oss_bucket is not None:
            result['ossBucket'] = self.oss_bucket

        if self.payment_duration_unit is not None:
            result['paymentDurationUnit'] = self.payment_duration_unit

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.ram_role_name is not None:
            result['ramRoleName'] = self.ram_role_name

        if self.release_type is not None:
            result['releaseType'] = self.release_type

        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec.to_map()

        result['tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['tag'].append(k1.to_map() if k1 else None)

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')

        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')

        if m.get('autoRenewPeriodUnit') is not None:
            self.auto_renew_period_unit = m.get('autoRenewPeriodUnit')

        if m.get('autoStartSessionCluster') is not None:
            self.auto_start_session_cluster = m.get('autoStartSessionCluster')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('dlfCatalogId') is not None:
            self.dlf_catalog_id = m.get('dlfCatalogId')

        if m.get('dlfType') is not None:
            self.dlf_type = m.get('dlfType')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('ossBucket') is not None:
            self.oss_bucket = m.get('ossBucket')

        if m.get('paymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('paymentDurationUnit')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('ramRoleName') is not None:
            self.ram_role_name = m.get('ramRoleName')

        if m.get('releaseType') is not None:
            self.release_type = m.get('releaseType')

        if m.get('resourceSpec') is not None:
            temp_model = main_models.CreateWorkspaceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('resourceSpec'))

        self.tag = []
        if m.get('tag') is not None:
            for k1 in m.get('tag'):
                temp_model = main_models.CreateWorkspaceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class CreateWorkspaceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

class CreateWorkspaceRequestResourceSpec(DaraModel):
    def __init__(
        self,
        cu: str = None,
    ):
        # The maximum resource quota for a workspace.
        self.cu = cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        return self

