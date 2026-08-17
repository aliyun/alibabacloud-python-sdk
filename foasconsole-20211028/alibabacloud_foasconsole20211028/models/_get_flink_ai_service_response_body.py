# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_foasconsole20211028 import models as main_models
from darabonba.model import DaraModel

class GetFlinkAiServiceResponseBody(DaraModel):
    def __init__(
        self,
        flink_ai_service_dto: main_models.GetFlinkAiServiceResponseBodyFlinkAiServiceDTO = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The Flink AI service data transfer object.
        self.flink_ai_service_dto = flink_ai_service_dto
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.flink_ai_service_dto:
            self.flink_ai_service_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flink_ai_service_dto is not None:
            result['FlinkAiServiceDTO'] = self.flink_ai_service_dto.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlinkAiServiceDTO') is not None:
            temp_model = main_models.GetFlinkAiServiceResponseBodyFlinkAiServiceDTO()
            self.flink_ai_service_dto = temp_model.from_map(m.get('FlinkAiServiceDTO'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetFlinkAiServiceResponseBodyFlinkAiServiceDTO(DaraModel):
    def __init__(
        self,
        deletion_protection: bool = None,
        flink_ai_instance_status: str = None,
        main_instance_id: str = None,
        region: str = None,
        resource_create_time: int = None,
    ):
        # Indicates whether deletion protection is enabled.
        self.deletion_protection = deletion_protection
        # The status of the Flink AI instance. Valid values:
        # - CLOSED: closed or not activated.
        # - WAITING: waiting to be activated after payment.
        # - OPENING: being activated.
        # - RUNNING: activated.
        # - CLOSING: being closed.
        # - DISABLE: overdue payment.
        self.flink_ai_instance_status = flink_ai_instance_status
        # The AI service order instance ID.
        self.main_instance_id = main_instance_id
        # The region ID.
        self.region = region
        # The time when the AI service was activated, in timestamp format (milliseconds).
        self.resource_create_time = resource_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.flink_ai_instance_status is not None:
            result['FlinkAiInstanceStatus'] = self.flink_ai_instance_status

        if self.main_instance_id is not None:
            result['MainInstanceId'] = self.main_instance_id

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_create_time is not None:
            result['ResourceCreateTime'] = self.resource_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('FlinkAiInstanceStatus') is not None:
            self.flink_ai_instance_status = m.get('FlinkAiInstanceStatus')

        if m.get('MainInstanceId') is not None:
            self.main_instance_id = m.get('MainInstanceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceCreateTime') is not None:
            self.resource_create_time = m.get('ResourceCreateTime')

        return self

