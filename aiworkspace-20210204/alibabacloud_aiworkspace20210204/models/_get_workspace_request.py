# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkspaceRequest(DaraModel):
    def __init__(
        self,
        extra_verbose_fields: str = None,
        verbose: bool = None,
    ):
        # A comma-separated string used to specify additional information to return. This field does not take effect.
        self.extra_verbose_fields = extra_verbose_fields
        # Specifies whether to display supplementary information such as the workspace owner. Valid values:
        # - false: Does not display supplementary information.
        # - true: Displays supplementary information.
        # Default value: false.
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra_verbose_fields is not None:
            result['ExtraVerboseFields'] = self.extra_verbose_fields

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraVerboseFields') is not None:
            self.extra_verbose_fields = m.get('ExtraVerboseFields')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        return self

