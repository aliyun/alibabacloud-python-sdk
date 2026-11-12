# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        member_to_update: str = None,
        update_type: str = None,
        body: str = None,
    ):
        # The client token used to ensure the idempotence of the request.
        self.client_token = client_token
        # Specifies whether to only precheck the request.
        # 
        # - true: sends a precheck request without performing the actual operation. If the precheck fails, the corresponding error is returned. If the precheck succeeds, the error code DryRunOperation is returned.
        # 
        # - false: sends a normal request. This is the default value.
        self.dry_run = dry_run
        # The type of the child service to update. Note: This parameter takes effect only for aggregated services.
        self.member_to_update = member_to_update
        # The update type of the service. Both merge and replace modes are supported. If this parameter is not specified, the merge mode is used by default.
        # 
        # - merge: the merge mode. If the original service configuration JSON is
        # `{"a":"b"}` and the updated configuration is `{"c":"d"}`, the final configuration in merge mode is `{"a":"b","c":"d"}`.
        # - replace: the replace mode. If the original service configuration JSON is
        # `{"a":"b"}` and the updated configuration is `{"c":"d"}`, the final configuration in replace mode is `{"c":"d"}`.
        self.update_type = update_type
        # The updated configuration. For more information about parameter settings, see [CreateService](https://help.aliyun.com/document_detail/412086.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.member_to_update is not None:
            result['MemberToUpdate'] = self.member_to_update

        if self.update_type is not None:
            result['UpdateType'] = self.update_type

        if self.body is not None:
            result['body'] = self.body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('MemberToUpdate') is not None:
            self.member_to_update = m.get('MemberToUpdate')

        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')

        if m.get('body') is not None:
            self.body = m.get('body')

        return self

