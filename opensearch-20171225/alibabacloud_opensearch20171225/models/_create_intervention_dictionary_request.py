# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInterventionDictionaryRequest(DaraModel):
    def __init__(
        self,
        analyzer_type: str = None,
        name: str = None,
        type: str = None,
        dry_run: bool = None,
    ):
        # The type of the analyzer. Valid values:
        # 
        # *   MODEL: model-based custom analyzer.
        # *   SYSTEM: system analyzer.
        # *   USER: custom analyzer.
        self.analyzer_type = analyzer_type
        # The name of the intervention dictionary.
        self.name = name
        # The type of the intervention dictionary. Valid values:
        # 
        # *   stopword: an intervention dictionary for stop word filtering.
        # *   synonym: an intervention dictionary for synonym configuration.
        # *   correction: an intervention dictionary for spelling correction.
        # *   category_prediction: an intervention dictionary for category prediction.
        # *   ner: an intervention dictionary for named entity recognition (NER).
        # *   term_weighting: an intervention dictionary for term weight analysis.
        # *   suggest_allowlist: a drop-down suggestion whitelist.
        # *   suggest_denylist: a drop-down suggestion blacklist.
        # *   hot_allowlist: a top search whitelist.
        # *   hot_denylist: a top search blacklist.
        # *   hint_allowlist: a hint whitelist.
        # *   hint_denylist: a hint blacklist.
        self.type = type
        # Specifies whether to perform only a dry run, without performing the actual request. Default value: false.
        # 
        # Valid values:
        # 
        # *   **true**
        # *   **false**
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

