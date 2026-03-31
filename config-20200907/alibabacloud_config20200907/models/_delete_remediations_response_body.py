# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class DeleteRemediationsResponseBody(DaraModel):
    def __init__(
        self,
        remediation_delete_results: List[main_models.DeleteRemediationsResponseBodyRemediationDeleteResults] = None,
        request_id: str = None,
    ):
        # The returned result.
        self.remediation_delete_results = remediation_delete_results
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.remediation_delete_results:
            for v1 in self.remediation_delete_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RemediationDeleteResults'] = []
        if self.remediation_delete_results is not None:
            for k1 in self.remediation_delete_results:
                result['RemediationDeleteResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remediation_delete_results = []
        if m.get('RemediationDeleteResults') is not None:
            for k1 in m.get('RemediationDeleteResults'):
                temp_model = main_models.DeleteRemediationsResponseBodyRemediationDeleteResults()
                self.remediation_delete_results.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DeleteRemediationsResponseBodyRemediationDeleteResults(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        remediation_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        # 
        # *   If the remediation template is deleted, no error code is returned.
        # *   If the remediation template fails to be deleted, an error code is returned. For more information about error codes, see [Error codes](https://error-center.alibabacloud.com/status/product/Config).
        self.error_message = error_message
        # The ID of the remediation template.
        self.remediation_id = remediation_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

