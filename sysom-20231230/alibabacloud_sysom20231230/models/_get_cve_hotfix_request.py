# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetCveHotfixRequest(DaraModel):
    def __init__(
        self,
        cve_ids: List[str] = None,
        kernel_versions: List[str] = None,
    ):
        # The list of CVE IDs.
        # 
        # This parameter is required.
        self.cve_ids = cve_ids
        # The list of full kernel versions.
        self.kernel_versions = kernel_versions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_ids is not None:
            result['cveIds'] = self.cve_ids

        if self.kernel_versions is not None:
            result['kernelVersions'] = self.kernel_versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cveIds') is not None:
            self.cve_ids = m.get('cveIds')

        if m.get('kernelVersions') is not None:
            self.kernel_versions = m.get('kernelVersions')

        return self

