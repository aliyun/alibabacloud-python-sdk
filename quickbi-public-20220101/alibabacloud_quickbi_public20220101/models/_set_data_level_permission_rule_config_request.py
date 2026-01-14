# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDataLevelPermissionRuleConfigRequest(DaraModel):
    def __init__(
        self,
        rule_model: str = None,
    ):
        # {
        #     "rule": "a5bb24da-****-a891683e14da",   // ID of the row and column permission rule; when provided, it modifies the row-level permission rule, otherwise, it adds a new one
        #     "cubeId": "7c7223ae-****-3c744528014b",  // Dataset ID
        #     "ruleName": "Test Row-Level Permission", // Name of the row-level permission rule
        #     "ruleLevelType": "ROW_LEVEL", // Type of row-level permission: ROW_LEVEL: Row-level permission, COLUMN_LEVEL: Column-level permission
        #     "ruleTargetScope": "ALL", // Target audience for the row-level permission rule: 1: Everyone, 2: Specific people
        #     "hitTakeEffect": 1, // Whether the rule takes effect after being hit (for column-level permissions): 1: Takes effect (default), 0: Does not take effect
        #     "ruleUsersModel": {
        #         "userGroups": [
        #             "9bd2c6440ac542****589f16bf12ca8178dd", // User group IDs for the target user groups
        #             "0d5fb19b-****-1248fc27ca51",
        #             "3d2c23d4-****-f6390f325c2d"
        #         ],
        #         "users": [
        #             "43342****3784358", // User IDs for the target users
        #             "Huang****2e3fa822"
        #         ]
        #     },
        #     "ruleContentModel": {
        #         "ruleContentType": "ROW_FIELD", // Type of the row and column permission rule
        #         "ruleContentJson": "{\\"conditionNode\\":{\\"caption\\":\\"Period\\",\\"isMeasure\\":false,\\"pathId\\":\\"7d3b***bc6\\",\\"relationOperator\\":\\"not-null\\",\\"name\\":\\"7d3b***bc6\\",\\"value\\":{\\"value\\":[\\"\\"],\\"valueType\\":\\"ENUM\\"}}}", // JSON string of the rule
        #         "ruleOriginConfigJson": "{\\"operator\\":\\"and\\",\\"operands\\":[{\\"labelName\\":\\"Period\\",\\"isValid\\":true,\\"uniqueId\\":\\"5\\",\\"fieldId\\":\\"7d3b***bc6\\",\\"error\\":false,\\"fieldType\\":\\"string\\",\\"defaultValue\\":{\\"selectType\\":\\"condition\\",\\"value\\":{\\"conditionOp\\":\\"not-null\\",\\"conditionValue\\":\\"\\"},\\"valueType\\":\\"ENUM\\"}}],\\"isRelation\\":true}" // JSON result used by the frontend template (specific to row-level permissions)
        #     }
        # }
        # 
        # This parameter is required.
        self.rule_model = rule_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_model is not None:
            result['RuleModel'] = self.rule_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleModel') is not None:
            self.rule_model = m.get('RuleModel')

        return self

