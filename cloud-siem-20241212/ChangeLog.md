2026-04-28 Version: 2.2.1
- Update API CreateDetectionRule: add request parameters AlertAttCkMapping.
- Update API CreateDetectionRule: add request parameters AlertLevelMapping.
- Update API CreateDetectionRule: add request parameters AlertTypeMapping.
- Update API ListDataSetRecords: add request parameters Filter.
- Update API ListDataSetRecords: add request parameters Order.
- Update API ListDataSetRecords: add request parameters OrderField.
- Update API ListDetectionRules: add response parameters Body.DetectionRules.$.AlertAttCkMapping.
- Update API ListDetectionRules: add response parameters Body.DetectionRules.$.AlertLevelMapping.
- Update API ListDetectionRules: add response parameters Body.DetectionRules.$.AlertTypeMapping.
- Update API UpdateDetectionRule: add request parameters AlertAttCkMapping.
- Update API UpdateDetectionRule: add request parameters AlertLevelMapping.
- Update API UpdateDetectionRule: add request parameters AlertTypeMapping.


2026-04-21 Version: 2.2.0
- Support API CreateAutoDisposeConfig.
- Support API ExecuteAutoDisposeRecords.
- Support API GetAutoDisposeConfig.
- Support API ListAutoDisposeEntities.
- Support API UpdateAutoDisposeConfig.
- Support API UpdateAutoDisposeRecord.


2026-04-15 Version: 2.1.0
- Support API CreateResponseRule.
- Support API DeleteResponseRule.
- Support API ListResponseRules.
- Support API UpdateResponseRule.


2026-04-15 Version: 2.1.0
- Support API CreateResponseRule.
- Support API DeleteResponseRule.
- Support API ListResponseRules.
- Support API UpdateResponseRule.


2026-03-25 Version: 2.0.2
- Update API ListDataIngestions: add request parameters NormalizationSchemaIds.


2026-02-10 Version: 2.0.1
- Update API ListTrafficStatistics: add request parameters TrafficType.


2026-02-04 Version: 2.0.0
- Support API CreateNormalizationSchema.
- Support API RefreshDataSource.
- Support API UpdateNormalizationSchema.
- Update API CreateDataSource: delete request parameters DataSourceStores.$.CreateTime.
- Update API CreateDataSource: delete request parameters DataSourceStores.$.UpdateTime.
- Update API CreateDataSource: delete request parameters UpdateTime.
- Update API CreateDetectionRule: add request parameters AlertDescription.
- Update API CreateDetectionRule: add request parameters AlertName.
- Update API CreateNormalizationRule: add request parameters ExtendFieldStoreMode.
- Update API GetIncident: add response parameters Body.Incident.Owner.
- Update API GetNormalizationRule: add response parameters Body.NormalizationRule.ExtendFieldStoreMode.
- Update API GetNormalizationSchema: add response parameters Body.NormalizationSchema.NormalizationSchemaDescription.
- Update API GetNormalizationSchema: add response parameters Body.NormalizationSchema.NormalizationSchemaFrom.
- Update API GetNormalizationSchema: add response parameters Body.NormalizationSchema.NormalizationSchemaReferences.
- Update API GetNormalizationSchema: add response parameters Body.NormalizationSchema.NormalizationFields.$.CreateTime.
- Update API GetNormalizationSchema: add response parameters Body.NormalizationSchema.NormalizationFields.$.NormalizationFieldFrom.
- Update API GetNormalizationSchema: add response parameters Body.NormalizationSchema.NormalizationFields.$.NormalizationFieldJsonIndexAll.
- Update API GetNormalizationSchema: add response parameters Body.NormalizationSchema.NormalizationFields.$.NormalizationFieldJsonKeys.
- Update API GetNormalizationSchema: add response parameters Body.NormalizationSchema.NormalizationFields.$.NormalizationFieldRequired.
- Update API GetNormalizationSchema: add response parameters Body.NormalizationSchema.NormalizationFields.$.NormalizationFieldTokenize.
- Update API GetNormalizationSchema: add response parameters Body.NormalizationSchema.NormalizationFields.$.UpdateTime.
- Update API ListDataSources: add response parameters Body.DataSources.$.DataSourceStores.$.DataSourceStoreStatusCode.
- Update API ListDetectionRules: add response parameters Body.DetectionRules.$.AlertDescription.
- Update API ListDetectionRules: add response parameters Body.DetectionRules.$.AlertName.
- Update API ListIncidents: add request parameters Owners.
- Update API ListIncidents: add response parameters Body.Incidents.$.DetectionRuleId.
- Update API ListIncidents: add response parameters Body.Incidents.$.Owner.
- Update API ListNormalizationFields: add response parameters Body.NormalizationFields.$.CreateTime.
- Update API ListNormalizationFields: add response parameters Body.NormalizationFields.$.NormalizationFieldFrom.
- Update API ListNormalizationFields: add response parameters Body.NormalizationFields.$.NormalizationFieldJsonIndexAll.
- Update API ListNormalizationFields: add response parameters Body.NormalizationFields.$.NormalizationFieldJsonKeys.
- Update API ListNormalizationFields: add response parameters Body.NormalizationFields.$.NormalizationFieldRequired.
- Update API ListNormalizationFields: add response parameters Body.NormalizationFields.$.NormalizationFieldTokenize.
- Update API ListNormalizationFields: add response parameters Body.NormalizationFields.$.UpdateTime.
- Update API ListNormalizationRules: add response parameters Body.NormalizationRules.$.ExtendFieldStoreMode.
- Update API ListNormalizationSchemas: add response parameters Body.NormalizationSchemas.$.CreateTime.
- Update API ListNormalizationSchemas: add response parameters Body.NormalizationSchemas.$.NormalizationSchemaDescription.
- Update API ListNormalizationSchemas: add response parameters Body.NormalizationSchemas.$.NormalizationSchemaFrom.
- Update API ListNormalizationSchemas: add response parameters Body.NormalizationSchemas.$.TargetLogStore.
- Update API ListNormalizationSchemas: add response parameters Body.NormalizationSchemas.$.TargetStoreView.
- Update API ListNormalizationSchemas: add response parameters Body.NormalizationSchemas.$.UpdateTime.
- Update API UpdateDetectionRule: add request parameters AlertDescription.
- Update API UpdateDetectionRule: add request parameters AlertName.
- Update API UpdateNormalizationRule: add request parameters ExtendFieldStoreMode.
- Update API UpdateNormalizationRule: add request parameters NormalizationCategoryId.
- Update API ValidateNormalizationRule: add request parameters ExtendFieldStoreMode.
- Update API ValidateNormalizationRule: add request parameters LogSample.
- Update API ValidateNormalizationRule: add request parameters NormalizationRuleExpression.
- Update API ValidateNormalizationRule: add request parameters NormalizationRuleMode.
- Update API ValidateNormalizationRule: add request parameters ProductId.
- Update API ValidateNormalizationRule: add request parameters VendorId.
- Update API ValidateNormalizationRule: add response parameters Body.ValidateResult.$.LogFieldName.
- Update API ValidateNormalizationRule: add response parameters Body.ValidateResult.$.LogFieldValue.
- Update API ValidateNormalizationRule: add response parameters Body.ValidateResult.$.NormalizationFieldFrom.
- Update API ValidateNormalizationRule: add response parameters Body.ValidateResult.$.NormalizationFieldReserved.
- Update API ValidateNormalizationRule: add response parameters Body.ValidateResult.$.NormalizationFieldType.
- Update API ValidateNormalizationRule: add response parameters Body.ValidateResult.$.NormalizationFieldValidationReason.
- Update API ValidateNormalizationRule: add response parameters Body.ValidateResult.$.NormalizationFieldValidationStatus.


2025-11-04 Version: 1.0.1
- Update API CreateDetectionRule: add request parameters DetectionRuleTemplateId.
- Update API CreateDetectionRule: add request parameters DetectionRuleTemplateVersion.
- Update API ListIncidents: add response parameters Body.Incidents.$.IncidentTags.


2025-10-14 Version: 1.0.0
- Generated python 2024-12-12 for cloud-siem.

