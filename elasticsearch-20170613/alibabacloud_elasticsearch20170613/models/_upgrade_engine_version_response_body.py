# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpgradeEngineVersionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.UpgradeEngineVersionResponseBodyResult] = None,
    ):
        # The verification information.
        self.request_id = request_id
        # The type of the error. Valid values:
        # 
        # *   clusterStatus: the health status of the cluster.
        # *   clusterConfigYml: Cluster YML File
        # *   clusterConfigPlugins: Cluster Configuration File
        # *   clusterResource: cluster resources
        # *   clusterSnapshot: cluster snapshot
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.UpgradeEngineVersionResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class UpgradeEngineVersionResponseBodyResult(DaraModel):
    def __init__(
        self,
        status: str = None,
        validate_result: List[main_models.UpgradeEngineVersionResponseBodyResultValidateResult] = None,
        validate_type: str = None,
    ):
        self.status = status
        # The error message returned.
        self.validate_result = validate_result
        # The error code returned if the request failed.
        self.validate_type = validate_type

    def validate(self):
        if self.validate_result:
            for v1 in self.validate_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        result['validateResult'] = []
        if self.validate_result is not None:
            for k1 in self.validate_result:
                result['validateResult'].append(k1.to_map() if k1 else None)

        if self.validate_type is not None:
            result['validateType'] = self.validate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        self.validate_result = []
        if m.get('validateResult') is not None:
            for k1 in m.get('validateResult'):
                temp_model = main_models.UpgradeEngineVersionResponseBodyResultValidateResult()
                self.validate_result.append(temp_model.from_map(k1))

        if m.get('validateType') is not None:
            self.validate_type = m.get('validateType')

        return self

class UpgradeEngineVersionResponseBodyResultValidateResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        error_type: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        # The verification is passed. Valid values:
        # 
        # *   success: through
        # *   failed: failed
        self.error_type = error_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.error_type is not None:
            result['errorType'] = self.error_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('errorType') is not None:
            self.error_type = m.get('errorType')

        return self

