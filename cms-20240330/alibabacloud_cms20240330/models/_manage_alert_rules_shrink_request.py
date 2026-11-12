# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManageAlertRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        body_shrink: str = None,
        call_source: str = None,
    ):
        # Specifies whether to perform a dry run. A dry run only validates the request and returns the validation result in dryRunResult without writing to the database, triggering template synchronization, or causing other side effects. Default value: false.
        self.dry_run = dry_run
        # The aggregated request body for managing alert rules. This body is shared by the CREATE, UPDATE, PATCH, and BATCH_DELETE operations. Specify the fields based on the action.
        self.body_shrink = body_shrink
        # The call source identifier. It identifies the internal integration channel to which the caller belongs, such as bailian, integrationCenter, or managed_service_for_prometheus, and is used to isolate traffic from different sources. Leave this parameter empty for regular OpenAPI calls.
        self.call_source = call_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.body_shrink is not None:
            result['body'] = self.body_shrink

        if self.call_source is not None:
            result['callSource'] = self.call_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('body') is not None:
            self.body_shrink = m.get('body')

        if m.get('callSource') is not None:
            self.call_source = m.get('callSource')

        return self

