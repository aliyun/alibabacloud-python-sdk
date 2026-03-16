# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateServiceInstanceNameRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        is_trial: bool = None,
        service_id: str = None,
        service_instance_name: str = None,
        service_version: str = None,
        template_name: str = None,
    ):
        self.client_token = client_token
        self.is_trial = is_trial
        # This parameter is required.
        self.service_id = service_id
        # This parameter is required.
        self.service_instance_name = service_instance_name
        self.service_version = service_version
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.is_trial is not None:
            result['IsTrial'] = self.is_trial

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_instance_name is not None:
            result['ServiceInstanceName'] = self.service_instance_name

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('IsTrial') is not None:
            self.is_trial = m.get('IsTrial')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInstanceName') is not None:
            self.service_instance_name = m.get('ServiceInstanceName')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

