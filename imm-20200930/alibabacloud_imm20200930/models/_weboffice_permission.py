# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WebofficePermission(DaraModel):
    def __init__(
        self,
        copy: bool = None,
        export: bool = None,
        history: bool = None,
        print: bool = None,
        readonly: bool = None,
        rename: bool = None,
    ):
        # Specifies whether the user has the copy permission. Valid values:
        # 
        # *   true
        # *   false
        self.copy = copy
        # Specifies whether the user has the permission to export the file as a PDF file. Valid values:
        # 
        # *   true: The user has the permission to export the file as a PDF file. If you set this parameter to true, you must set the Print parameter to true.
        # *   false: The user does not have the permission to export the file as a PDF file.
        self.export = export
        # Specifies whether the user has the permission to view historical versions. Valid values:
        # 
        # *   true
        # *   false
        self.history = history
        # Specifies whether the user has the printing permission. Valid values:
        # 
        # *   true
        # *   false
        self.print = print
        # Specifies whether the user has read-only access to the file. Valid values:
        # 
        # *   true
        # *   false
        self.readonly = readonly
        # Specifies whether the user has the permission to rename a file. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  You can query the operation information only based a notification sent to Simple Message Queue (SMQ). A rename event is included in the notification.
        self.rename = rename

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.copy is not None:
            result['Copy'] = self.copy

        if self.export is not None:
            result['Export'] = self.export

        if self.history is not None:
            result['History'] = self.history

        if self.print is not None:
            result['Print'] = self.print

        if self.readonly is not None:
            result['Readonly'] = self.readonly

        if self.rename is not None:
            result['Rename'] = self.rename

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Copy') is not None:
            self.copy = m.get('Copy')

        if m.get('Export') is not None:
            self.export = m.get('Export')

        if m.get('History') is not None:
            self.history = m.get('History')

        if m.get('Print') is not None:
            self.print = m.get('Print')

        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')

        if m.get('Rename') is not None:
            self.rename = m.get('Rename')

        return self

