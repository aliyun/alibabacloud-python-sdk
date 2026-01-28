# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryFailingReasonListForQualificationRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        limit: int = None,
        qualification_type: str = None,
        user_client_ip: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.lang = lang
        # This parameter is required.
        self.limit = limit
        # This parameter is required.
        self.qualification_type = qualification_type
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.qualification_type is not None:
            result['QualificationType'] = self.qualification_type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('QualificationType') is not None:
            self.qualification_type = m.get('QualificationType')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

