# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeKernelReleaseNotesResponseBody(DaraModel):
    def __init__(
        self,
        release_notes: main_models.DescribeKernelReleaseNotesResponseBodyReleaseNotes = None,
        request_id: str = None,
    ):
        # The list of the version release notes.
        self.release_notes = release_notes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.release_notes:
            self.release_notes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.release_notes is not None:
            result['ReleaseNotes'] = self.release_notes.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReleaseNotes') is not None:
            temp_model = main_models.DescribeKernelReleaseNotesResponseBodyReleaseNotes()
            self.release_notes = temp_model.from_map(m.get('ReleaseNotes'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeKernelReleaseNotesResponseBodyReleaseNotes(DaraModel):
    def __init__(
        self,
        release_note: List[main_models.DescribeKernelReleaseNotesResponseBodyReleaseNotesReleaseNote] = None,
    ):
        self.release_note = release_note

    def validate(self):
        if self.release_note:
            for v1 in self.release_note:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReleaseNote'] = []
        if self.release_note is not None:
            for k1 in self.release_note:
                result['ReleaseNote'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.release_note = []
        if m.get('ReleaseNote') is not None:
            for k1 in m.get('ReleaseNote'):
                temp_model = main_models.DescribeKernelReleaseNotesResponseBodyReleaseNotesReleaseNote()
                self.release_note.append(temp_model.from_map(k1))

        return self

class DescribeKernelReleaseNotesResponseBodyReleaseNotesReleaseNote(DaraModel):
    def __init__(
        self,
        kernel_version: str = None,
        release_note: str = None,
    ):
        # The version number.
        self.kernel_version = kernel_version
        # The release notes.
        self.release_note = release_note

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version

        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        return self

