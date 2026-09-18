# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManageAlertRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        call_source: str = None,
    ):
        # The request body for managing alert rules. This body is shared by the CREATE, UPDATE, PATCH, and BATCH_DELETE actions. Specify the fields based on the action.
        self.body_shrink = body_shrink
        # The identifier of the call source, which specifies the internal integration channel to which the caller belongs (such as bailian, integrationCenter, or managed_service_for_prometheus). This parameter is used to isolate traffic from different call sources. You do not need to specify this parameter for regular OpenAPI calls.
        self.call_source = call_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_shrink is not None:
            result['body'] = self.body_shrink

        if self.call_source is not None:
            result['callSource'] = self.call_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')

        if m.get('callSource') is not None:
            self.call_source = m.get('callSource')

        return self

