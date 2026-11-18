# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetApplicationTemplateRequest(DaraModel):
    def __init__(
        self,
        application_template_id: str = None,
        built_in_application_action_type: str = None,
    ):
        # The ID of the application template to query. The template must exist within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.application_template_id = application_template_id
        # The return scope for built-in application actions. Valid values:
        # - **Custom**: returns only applications whose actions have been customized by the user. This is the default value.
        # - **All**: returns all built-in applications.
        # The priority of action effectiveness is: user customization > template default > application library default.
        self.built_in_application_action_type = built_in_application_action_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        if self.built_in_application_action_type is not None:
            result['BuiltInApplicationActionType'] = self.built_in_application_action_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        if m.get('BuiltInApplicationActionType') is not None:
            self.built_in_application_action_type = m.get('BuiltInApplicationActionType')

        return self

