# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EvaluatorVariableExtractorMappingValue(DaraModel):
    def __init__(
        self,
        origin_field: str = None,
        type: str = None,
        expression: str = None,
    ):
        # The evaluation data field from which content is extracted. The extraction expression is applied to the content of this field. Required when saving with the evaluation task. For the trial run API, this parameter can be omitted and the backend derives it from the expression. Multiple variables can share the same source field.
        self.origin_field = origin_field
        # The extraction method. jsonpath extracts values from the JSON content of the field by using JSONPath. regex performs regular expression matching on the full text of the field. When capturing groups are present, the first capturing group is returned. When no capturing group is present, the entire match is returned.
        self.type = type
        # The extraction expression. Its meaning is determined by type. When type is jsonpath, specify a JSONPath expression. You can use either a relative path relative to originField (such as $.order.expected) or an absolute path from the root (such as $trace.output.order.expected). When type is regex, specify a regular expression. Note that backslashes must be escaped in JSON. The expression syntax is validated upon saving. For regular expressions, RE2 compatibility is additionally validated. Patterns such as lookahead assertions, lookbehind assertions, backreferences, named groups, atomic groups, and possessive quantifiers are rejected.
        self.expression = expression

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.origin_field is not None:
            result['originField'] = self.origin_field

        if self.type is not None:
            result['type'] = self.type

        if self.expression is not None:
            result['expression'] = self.expression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originField') is not None:
            self.origin_field = m.get('originField')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        return self

