# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class UpdatePolarClawSkillResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        config: main_models.UpdatePolarClawSkillResponseBodyConfig = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        skill_key: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The updated Skill configuration. Sensitive values are masked.
        self.config = config
        # The response message.
        self.message = message
        # Indicates whether the operation is successful.
        self.ok = ok
        # Id of the request
        self.request_id = request_id
        # The Skill identifier key.
        self.skill_key = skill_key

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.ok is not None:
            result['Ok'] = self.ok

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.skill_key is not None:
            result['SkillKey'] = self.skill_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Config') is not None:
            temp_model = main_models.UpdatePolarClawSkillResponseBodyConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Ok') is not None:
            self.ok = m.get('Ok')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SkillKey') is not None:
            self.skill_key = m.get('SkillKey')

        return self

class UpdatePolarClawSkillResponseBodyConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        env: Dict[str, str] = None,
    ):
        # Specifies whether to enable the Skill.
        self.enabled = enabled
        # The environment variable configuration.
        self.env = env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.env is not None:
            result['Env'] = self.env

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        return self

