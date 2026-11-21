# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ManageAlertRulesRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        body: main_models.ManageAlertRulesUnifiedActionInput = None,
        call_source: str = None,
    ):
        # Specifies whether to perform a dry run. If you set this parameter to true, the system only validates the request and returns the validation result in dryRunResult. No side effects, such as database writes or template synchronization, are triggered. Default value: false.
        self.dry_run = dry_run
        # The aggregated request body for managing alert rules. This body is shared by the CREATE, UPDATE, PATCH, and BATCH_DELETE operations. Specify the fields based on the action.
        self.body = body
        # The call source identifier that specifies the internal integration channel of the caller, such as bailian, integrationCenter, or managed_service_for_prometheus. This parameter is used to isolate traffic from different sources. You do not need to specify this parameter for standard OpenAPI calls.
        self.call_source = call_source

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.call_source is not None:
            result['callSource'] = self.call_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('body') is not None:
            temp_model = main_models.ManageAlertRulesUnifiedActionInput()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('callSource') is not None:
            self.call_source = m.get('callSource')

        return self

