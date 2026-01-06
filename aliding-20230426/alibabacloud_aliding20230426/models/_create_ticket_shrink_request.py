# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTicketShrinkRequest(DaraModel):
    def __init__(
        self,
        custom_fields: str = None,
        notify_shrink: str = None,
        open_team_id: str = None,
        open_template_biz_id: str = None,
        processor_user_ids_shrink: str = None,
        scene: str = None,
        scene_context_shrink: str = None,
        tenant_context_shrink: str = None,
        title: str = None,
    ):
        self.custom_fields = custom_fields
        self.notify_shrink = notify_shrink
        # This parameter is required.
        self.open_team_id = open_team_id
        # This parameter is required.
        self.open_template_biz_id = open_template_biz_id
        # This parameter is required.
        self.processor_user_ids_shrink = processor_user_ids_shrink
        # This parameter is required.
        self.scene = scene
        self.scene_context_shrink = scene_context_shrink
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_fields is not None:
            result['CustomFields'] = self.custom_fields

        if self.notify_shrink is not None:
            result['Notify'] = self.notify_shrink

        if self.open_team_id is not None:
            result['OpenTeamId'] = self.open_team_id

        if self.open_template_biz_id is not None:
            result['OpenTemplateBizId'] = self.open_template_biz_id

        if self.processor_user_ids_shrink is not None:
            result['ProcessorUserIds'] = self.processor_user_ids_shrink

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.scene_context_shrink is not None:
            result['SceneContext'] = self.scene_context_shrink

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomFields') is not None:
            self.custom_fields = m.get('CustomFields')

        if m.get('Notify') is not None:
            self.notify_shrink = m.get('Notify')

        if m.get('OpenTeamId') is not None:
            self.open_team_id = m.get('OpenTeamId')

        if m.get('OpenTemplateBizId') is not None:
            self.open_template_biz_id = m.get('OpenTemplateBizId')

        if m.get('ProcessorUserIds') is not None:
            self.processor_user_ids_shrink = m.get('ProcessorUserIds')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SceneContext') is not None:
            self.scene_context_shrink = m.get('SceneContext')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

