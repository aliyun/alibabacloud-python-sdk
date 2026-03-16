# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class RenewServiceInstanceResourcesResponseBody(DaraModel):
    def __init__(
        self,
        failure_details: List[main_models.RenewServiceInstanceResourcesResponseBodyFailureDetails] = None,
        renewal_result: main_models.RenewServiceInstanceResourcesResponseBodyRenewalResult = None,
        request_id: str = None,
    ):
        # Details of failed renewals.
        self.failure_details = failure_details
        # Renewal result.
        self.renewal_result = renewal_result
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.failure_details:
            for v1 in self.failure_details:
                 if v1:
                    v1.validate()
        if self.renewal_result:
            self.renewal_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailureDetails'] = []
        if self.failure_details is not None:
            for k1 in self.failure_details:
                result['FailureDetails'].append(k1.to_map() if k1 else None)

        if self.renewal_result is not None:
            result['RenewalResult'] = self.renewal_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failure_details = []
        if m.get('FailureDetails') is not None:
            for k1 in m.get('FailureDetails'):
                temp_model = main_models.RenewServiceInstanceResourcesResponseBodyFailureDetails()
                self.failure_details.append(temp_model.from_map(k1))

        if m.get('RenewalResult') is not None:
            temp_model = main_models.RenewServiceInstanceResourcesResponseBodyRenewalResult()
            self.renewal_result = temp_model.from_map(m.get('RenewalResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RenewServiceInstanceResourcesResponseBodyRenewalResult(DaraModel):
    def __init__(
        self,
        failed: int = None,
        succeeded: int = None,
        total_count: int = None,
    ):
        # Number of failed renewals.
        self.failed = failed
        # Number of successfully renewed resources.
        self.succeeded = succeeded
        # Number of renewed resources.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class RenewServiceInstanceResourcesResponseBodyFailureDetails(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        resource_arn: str = None,
    ):
        # Error code.
        self.error_code = error_code
        # Error message.
        self.error_message = error_message
        # Resource ARN (Aliyun Resource Name).
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        return self

