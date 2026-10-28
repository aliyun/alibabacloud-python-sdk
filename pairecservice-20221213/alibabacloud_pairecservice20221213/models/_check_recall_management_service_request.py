# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class CheckRecallManagementServiceRequest(DaraModel):
    def __init__(
        self,
        context_params: Dict[str, Any] = None,
        exposure_list: List[str] = None,
        instance_id: str = None,
        recall_management_service_version_id: str = None,
        recalls: Dict[str, Any] = None,
        retain_fields: List[str] = None,
        uid: str = None,
    ):
        # The context parameters.
        self.context_params = context_params
        # The exposure list.
        self.exposure_list = exposure_list
        # The instance ID.
        self.instance_id = instance_id
        # The recall management service version ID.
        self.recall_management_service_version_id = recall_management_service_version_id
        # The recall data details.
        self.recalls = recalls
        # The retained fields.
        self.retain_fields = retain_fields
        # The user ID.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_params is not None:
            result['ContextParams'] = self.context_params

        if self.exposure_list is not None:
            result['ExposureList'] = self.exposure_list

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.recall_management_service_version_id is not None:
            result['RecallManagementServiceVersionId'] = self.recall_management_service_version_id

        if self.recalls is not None:
            result['Recalls'] = self.recalls

        if self.retain_fields is not None:
            result['RetainFields'] = self.retain_fields

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextParams') is not None:
            self.context_params = m.get('ContextParams')

        if m.get('ExposureList') is not None:
            self.exposure_list = m.get('ExposureList')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RecallManagementServiceVersionId') is not None:
            self.recall_management_service_version_id = m.get('RecallManagementServiceVersionId')

        if m.get('Recalls') is not None:
            self.recalls = m.get('Recalls')

        if m.get('RetainFields') is not None:
            self.retain_fields = m.get('RetainFields')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

