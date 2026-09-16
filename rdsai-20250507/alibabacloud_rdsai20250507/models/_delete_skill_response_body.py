# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSkillResponseBody(DaraModel):
    def __init__(
        self,
        catalog_revision: int = None,
        deleted: bool = None,
        request_id: str = None,
        result: str = None,
        skill_id: str = None,
    ):
        # The Skill catalog revision number.
        self.catalog_revision = catalog_revision
        # Indicates whether the Skill is deleted.
        self.deleted = deleted
        # The unique identifier of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result
        # The ID of the deleted Skill.
        self.skill_id = skill_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_revision is not None:
            result['CatalogRevision'] = self.catalog_revision

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogRevision') is not None:
            self.catalog_revision = m.get('CatalogRevision')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        return self

