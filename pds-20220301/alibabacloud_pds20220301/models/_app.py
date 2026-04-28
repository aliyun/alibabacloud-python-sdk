# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class App(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_secret: str = None,
        created_at: str = None,
        description: str = None,
        logo: str = None,
        provider: str = None,
        redirect_uri: str = None,
        scope: List[str] = None,
        stage: str = None,
        type: str = None,
        updated_at: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_secret = app_secret
        self.created_at = created_at
        self.description = description
        self.logo = logo
        self.provider = provider
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.stage = stage
        self.type = type
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['app_id'] = self.app_id

        if self.app_name is not None:
            result['app_name'] = self.app_name

        if self.app_secret is not None:
            result['app_secret'] = self.app_secret

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.logo is not None:
            result['logo'] = self.logo

        if self.provider is not None:
            result['provider'] = self.provider

        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri

        if self.scope is not None:
            result['scope'] = self.scope

        if self.stage is not None:
            result['stage'] = self.stage

        if self.type is not None:
            result['type'] = self.type

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')

        if m.get('app_name') is not None:
            self.app_name = m.get('app_name')

        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('logo') is not None:
            self.logo = m.get('logo')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('stage') is not None:
            self.stage = m.get('stage')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

