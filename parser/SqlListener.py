# Generated from Sql.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SqlParser import SqlParser
else:
    from SqlParser import SqlParser

# This class defines a complete listener for a parse tree produced by SqlParser.
class SqlListener(ParseTreeListener):

    # Enter a parse tree produced by SqlParser#parse.
    def enterParse(self, ctx:SqlParser.ParseContext):
        pass

    # Exit a parse tree produced by SqlParser#parse.
    def exitParse(self, ctx:SqlParser.ParseContext):
        pass


    # Enter a parse tree produced by SqlParser#error.
    def enterError(self, ctx:SqlParser.ErrorContext):
        pass

    # Exit a parse tree produced by SqlParser#error.
    def exitError(self, ctx:SqlParser.ErrorContext):
        pass


    # Enter a parse tree produced by SqlParser#sql_stmt_list.
    def enterSql_stmt_list(self, ctx:SqlParser.Sql_stmt_listContext):
        pass

    # Exit a parse tree produced by SqlParser#sql_stmt_list.
    def exitSql_stmt_list(self, ctx:SqlParser.Sql_stmt_listContext):
        pass


    # Enter a parse tree produced by SqlParser#sql_stmt.
    def enterSql_stmt(self, ctx:SqlParser.Sql_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#sql_stmt.
    def exitSql_stmt(self, ctx:SqlParser.Sql_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#alter_table_stmt.
    def enterAlter_table_stmt(self, ctx:SqlParser.Alter_table_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#alter_table_stmt.
    def exitAlter_table_stmt(self, ctx:SqlParser.Alter_table_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#alter_table_add_constraint.
    def enterAlter_table_add_constraint(self, ctx:SqlParser.Alter_table_add_constraintContext):
        pass

    # Exit a parse tree produced by SqlParser#alter_table_add_constraint.
    def exitAlter_table_add_constraint(self, ctx:SqlParser.Alter_table_add_constraintContext):
        pass


    # Enter a parse tree produced by SqlParser#alter_table_add.
    def enterAlter_table_add(self, ctx:SqlParser.Alter_table_addContext):
        pass

    # Exit a parse tree produced by SqlParser#alter_table_add.
    def exitAlter_table_add(self, ctx:SqlParser.Alter_table_addContext):
        pass


    # Enter a parse tree produced by SqlParser#analyze_stmt.
    def enterAnalyze_stmt(self, ctx:SqlParser.Analyze_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#analyze_stmt.
    def exitAnalyze_stmt(self, ctx:SqlParser.Analyze_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#attach_stmt.
    def enterAttach_stmt(self, ctx:SqlParser.Attach_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#attach_stmt.
    def exitAttach_stmt(self, ctx:SqlParser.Attach_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#begin_stmt.
    def enterBegin_stmt(self, ctx:SqlParser.Begin_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#begin_stmt.
    def exitBegin_stmt(self, ctx:SqlParser.Begin_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#commit_stmt.
    def enterCommit_stmt(self, ctx:SqlParser.Commit_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#commit_stmt.
    def exitCommit_stmt(self, ctx:SqlParser.Commit_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#compound_select_stmt.
    def enterCompound_select_stmt(self, ctx:SqlParser.Compound_select_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#compound_select_stmt.
    def exitCompound_select_stmt(self, ctx:SqlParser.Compound_select_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#create_index_stmt.
    def enterCreate_index_stmt(self, ctx:SqlParser.Create_index_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#create_index_stmt.
    def exitCreate_index_stmt(self, ctx:SqlParser.Create_index_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#create_table_stmt.
    def enterCreate_table_stmt(self, ctx:SqlParser.Create_table_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#create_table_stmt.
    def exitCreate_table_stmt(self, ctx:SqlParser.Create_table_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#create_trigger_stmt.
    def enterCreate_trigger_stmt(self, ctx:SqlParser.Create_trigger_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#create_trigger_stmt.
    def exitCreate_trigger_stmt(self, ctx:SqlParser.Create_trigger_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#create_view_stmt.
    def enterCreate_view_stmt(self, ctx:SqlParser.Create_view_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#create_view_stmt.
    def exitCreate_view_stmt(self, ctx:SqlParser.Create_view_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#create_virtual_table_stmt.
    def enterCreate_virtual_table_stmt(self, ctx:SqlParser.Create_virtual_table_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#create_virtual_table_stmt.
    def exitCreate_virtual_table_stmt(self, ctx:SqlParser.Create_virtual_table_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#delete_stmt.
    def enterDelete_stmt(self, ctx:SqlParser.Delete_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#delete_stmt.
    def exitDelete_stmt(self, ctx:SqlParser.Delete_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#delete_stmt_limited.
    def enterDelete_stmt_limited(self, ctx:SqlParser.Delete_stmt_limitedContext):
        pass

    # Exit a parse tree produced by SqlParser#delete_stmt_limited.
    def exitDelete_stmt_limited(self, ctx:SqlParser.Delete_stmt_limitedContext):
        pass


    # Enter a parse tree produced by SqlParser#detach_stmt.
    def enterDetach_stmt(self, ctx:SqlParser.Detach_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#detach_stmt.
    def exitDetach_stmt(self, ctx:SqlParser.Detach_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#drop_index_stmt.
    def enterDrop_index_stmt(self, ctx:SqlParser.Drop_index_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#drop_index_stmt.
    def exitDrop_index_stmt(self, ctx:SqlParser.Drop_index_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#drop_table_stmt.
    def enterDrop_table_stmt(self, ctx:SqlParser.Drop_table_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#drop_table_stmt.
    def exitDrop_table_stmt(self, ctx:SqlParser.Drop_table_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#drop_trigger_stmt.
    def enterDrop_trigger_stmt(self, ctx:SqlParser.Drop_trigger_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#drop_trigger_stmt.
    def exitDrop_trigger_stmt(self, ctx:SqlParser.Drop_trigger_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#drop_view_stmt.
    def enterDrop_view_stmt(self, ctx:SqlParser.Drop_view_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#drop_view_stmt.
    def exitDrop_view_stmt(self, ctx:SqlParser.Drop_view_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#factored_select_stmt.
    def enterFactored_select_stmt(self, ctx:SqlParser.Factored_select_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#factored_select_stmt.
    def exitFactored_select_stmt(self, ctx:SqlParser.Factored_select_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#insert_stmt.
    def enterInsert_stmt(self, ctx:SqlParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#insert_stmt.
    def exitInsert_stmt(self, ctx:SqlParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#pragma_stmt.
    def enterPragma_stmt(self, ctx:SqlParser.Pragma_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#pragma_stmt.
    def exitPragma_stmt(self, ctx:SqlParser.Pragma_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#reindex_stmt.
    def enterReindex_stmt(self, ctx:SqlParser.Reindex_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#reindex_stmt.
    def exitReindex_stmt(self, ctx:SqlParser.Reindex_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#release_stmt.
    def enterRelease_stmt(self, ctx:SqlParser.Release_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#release_stmt.
    def exitRelease_stmt(self, ctx:SqlParser.Release_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#rollback_stmt.
    def enterRollback_stmt(self, ctx:SqlParser.Rollback_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#rollback_stmt.
    def exitRollback_stmt(self, ctx:SqlParser.Rollback_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#savepoint_stmt.
    def enterSavepoint_stmt(self, ctx:SqlParser.Savepoint_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#savepoint_stmt.
    def exitSavepoint_stmt(self, ctx:SqlParser.Savepoint_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#simple_select_stmt.
    def enterSimple_select_stmt(self, ctx:SqlParser.Simple_select_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#simple_select_stmt.
    def exitSimple_select_stmt(self, ctx:SqlParser.Simple_select_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#select_stmt.
    def enterSelect_stmt(self, ctx:SqlParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#select_stmt.
    def exitSelect_stmt(self, ctx:SqlParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#select_or_values.
    def enterSelect_or_values(self, ctx:SqlParser.Select_or_valuesContext):
        pass

    # Exit a parse tree produced by SqlParser#select_or_values.
    def exitSelect_or_values(self, ctx:SqlParser.Select_or_valuesContext):
        pass


    # Enter a parse tree produced by SqlParser#update_stmt.
    def enterUpdate_stmt(self, ctx:SqlParser.Update_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#update_stmt.
    def exitUpdate_stmt(self, ctx:SqlParser.Update_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#update_stmt_limited.
    def enterUpdate_stmt_limited(self, ctx:SqlParser.Update_stmt_limitedContext):
        pass

    # Exit a parse tree produced by SqlParser#update_stmt_limited.
    def exitUpdate_stmt_limited(self, ctx:SqlParser.Update_stmt_limitedContext):
        pass


    # Enter a parse tree produced by SqlParser#vacuum_stmt.
    def enterVacuum_stmt(self, ctx:SqlParser.Vacuum_stmtContext):
        pass

    # Exit a parse tree produced by SqlParser#vacuum_stmt.
    def exitVacuum_stmt(self, ctx:SqlParser.Vacuum_stmtContext):
        pass


    # Enter a parse tree produced by SqlParser#column_def.
    def enterColumn_def(self, ctx:SqlParser.Column_defContext):
        pass

    # Exit a parse tree produced by SqlParser#column_def.
    def exitColumn_def(self, ctx:SqlParser.Column_defContext):
        pass


    # Enter a parse tree produced by SqlParser#type_name.
    def enterType_name(self, ctx:SqlParser.Type_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#type_name.
    def exitType_name(self, ctx:SqlParser.Type_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#column_constraint.
    def enterColumn_constraint(self, ctx:SqlParser.Column_constraintContext):
        pass

    # Exit a parse tree produced by SqlParser#column_constraint.
    def exitColumn_constraint(self, ctx:SqlParser.Column_constraintContext):
        pass


    # Enter a parse tree produced by SqlParser#column_constraint_primary_key.
    def enterColumn_constraint_primary_key(self, ctx:SqlParser.Column_constraint_primary_keyContext):
        pass

    # Exit a parse tree produced by SqlParser#column_constraint_primary_key.
    def exitColumn_constraint_primary_key(self, ctx:SqlParser.Column_constraint_primary_keyContext):
        pass


    # Enter a parse tree produced by SqlParser#column_constraint_foreign_key.
    def enterColumn_constraint_foreign_key(self, ctx:SqlParser.Column_constraint_foreign_keyContext):
        pass

    # Exit a parse tree produced by SqlParser#column_constraint_foreign_key.
    def exitColumn_constraint_foreign_key(self, ctx:SqlParser.Column_constraint_foreign_keyContext):
        pass


    # Enter a parse tree produced by SqlParser#column_constraint_not_null.
    def enterColumn_constraint_not_null(self, ctx:SqlParser.Column_constraint_not_nullContext):
        pass

    # Exit a parse tree produced by SqlParser#column_constraint_not_null.
    def exitColumn_constraint_not_null(self, ctx:SqlParser.Column_constraint_not_nullContext):
        pass


    # Enter a parse tree produced by SqlParser#column_constraint_null.
    def enterColumn_constraint_null(self, ctx:SqlParser.Column_constraint_nullContext):
        pass

    # Exit a parse tree produced by SqlParser#column_constraint_null.
    def exitColumn_constraint_null(self, ctx:SqlParser.Column_constraint_nullContext):
        pass


    # Enter a parse tree produced by SqlParser#column_default.
    def enterColumn_default(self, ctx:SqlParser.Column_defaultContext):
        pass

    # Exit a parse tree produced by SqlParser#column_default.
    def exitColumn_default(self, ctx:SqlParser.Column_defaultContext):
        pass


    # Enter a parse tree produced by SqlParser#column_default_value.
    def enterColumn_default_value(self, ctx:SqlParser.Column_default_valueContext):
        pass

    # Exit a parse tree produced by SqlParser#column_default_value.
    def exitColumn_default_value(self, ctx:SqlParser.Column_default_valueContext):
        pass


    # Enter a parse tree produced by SqlParser#conflict_clause.
    def enterConflict_clause(self, ctx:SqlParser.Conflict_clauseContext):
        pass

    # Exit a parse tree produced by SqlParser#conflict_clause.
    def exitConflict_clause(self, ctx:SqlParser.Conflict_clauseContext):
        pass


    # Enter a parse tree produced by SqlParser#expr.
    def enterExpr(self, ctx:SqlParser.ExprContext):
        pass

    # Exit a parse tree produced by SqlParser#expr.
    def exitExpr(self, ctx:SqlParser.ExprContext):
        pass


    # Enter a parse tree produced by SqlParser#foreign_key_clause.
    def enterForeign_key_clause(self, ctx:SqlParser.Foreign_key_clauseContext):
        pass

    # Exit a parse tree produced by SqlParser#foreign_key_clause.
    def exitForeign_key_clause(self, ctx:SqlParser.Foreign_key_clauseContext):
        pass


    # Enter a parse tree produced by SqlParser#fk_target_column_name.
    def enterFk_target_column_name(self, ctx:SqlParser.Fk_target_column_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#fk_target_column_name.
    def exitFk_target_column_name(self, ctx:SqlParser.Fk_target_column_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#raise_function.
    def enterRaise_function(self, ctx:SqlParser.Raise_functionContext):
        pass

    # Exit a parse tree produced by SqlParser#raise_function.
    def exitRaise_function(self, ctx:SqlParser.Raise_functionContext):
        pass


    # Enter a parse tree produced by SqlParser#indexed_column.
    def enterIndexed_column(self, ctx:SqlParser.Indexed_columnContext):
        pass

    # Exit a parse tree produced by SqlParser#indexed_column.
    def exitIndexed_column(self, ctx:SqlParser.Indexed_columnContext):
        pass


    # Enter a parse tree produced by SqlParser#table_constraint.
    def enterTable_constraint(self, ctx:SqlParser.Table_constraintContext):
        pass

    # Exit a parse tree produced by SqlParser#table_constraint.
    def exitTable_constraint(self, ctx:SqlParser.Table_constraintContext):
        pass


    # Enter a parse tree produced by SqlParser#table_constraint_primary_key.
    def enterTable_constraint_primary_key(self, ctx:SqlParser.Table_constraint_primary_keyContext):
        pass

    # Exit a parse tree produced by SqlParser#table_constraint_primary_key.
    def exitTable_constraint_primary_key(self, ctx:SqlParser.Table_constraint_primary_keyContext):
        pass


    # Enter a parse tree produced by SqlParser#table_constraint_foreign_key.
    def enterTable_constraint_foreign_key(self, ctx:SqlParser.Table_constraint_foreign_keyContext):
        pass

    # Exit a parse tree produced by SqlParser#table_constraint_foreign_key.
    def exitTable_constraint_foreign_key(self, ctx:SqlParser.Table_constraint_foreign_keyContext):
        pass


    # Enter a parse tree produced by SqlParser#table_constraint_unique.
    def enterTable_constraint_unique(self, ctx:SqlParser.Table_constraint_uniqueContext):
        pass

    # Exit a parse tree produced by SqlParser#table_constraint_unique.
    def exitTable_constraint_unique(self, ctx:SqlParser.Table_constraint_uniqueContext):
        pass


    # Enter a parse tree produced by SqlParser#table_constraint_key.
    def enterTable_constraint_key(self, ctx:SqlParser.Table_constraint_keyContext):
        pass

    # Exit a parse tree produced by SqlParser#table_constraint_key.
    def exitTable_constraint_key(self, ctx:SqlParser.Table_constraint_keyContext):
        pass


    # Enter a parse tree produced by SqlParser#fk_origin_column_name.
    def enterFk_origin_column_name(self, ctx:SqlParser.Fk_origin_column_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#fk_origin_column_name.
    def exitFk_origin_column_name(self, ctx:SqlParser.Fk_origin_column_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#with_clause.
    def enterWith_clause(self, ctx:SqlParser.With_clauseContext):
        pass

    # Exit a parse tree produced by SqlParser#with_clause.
    def exitWith_clause(self, ctx:SqlParser.With_clauseContext):
        pass


    # Enter a parse tree produced by SqlParser#qualified_table_name.
    def enterQualified_table_name(self, ctx:SqlParser.Qualified_table_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#qualified_table_name.
    def exitQualified_table_name(self, ctx:SqlParser.Qualified_table_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#ordering_term.
    def enterOrdering_term(self, ctx:SqlParser.Ordering_termContext):
        pass

    # Exit a parse tree produced by SqlParser#ordering_term.
    def exitOrdering_term(self, ctx:SqlParser.Ordering_termContext):
        pass


    # Enter a parse tree produced by SqlParser#pragma_value.
    def enterPragma_value(self, ctx:SqlParser.Pragma_valueContext):
        pass

    # Exit a parse tree produced by SqlParser#pragma_value.
    def exitPragma_value(self, ctx:SqlParser.Pragma_valueContext):
        pass


    # Enter a parse tree produced by SqlParser#common_table_expression.
    def enterCommon_table_expression(self, ctx:SqlParser.Common_table_expressionContext):
        pass

    # Exit a parse tree produced by SqlParser#common_table_expression.
    def exitCommon_table_expression(self, ctx:SqlParser.Common_table_expressionContext):
        pass


    # Enter a parse tree produced by SqlParser#result_column.
    def enterResult_column(self, ctx:SqlParser.Result_columnContext):
        pass

    # Exit a parse tree produced by SqlParser#result_column.
    def exitResult_column(self, ctx:SqlParser.Result_columnContext):
        pass


    # Enter a parse tree produced by SqlParser#table_or_subquery.
    def enterTable_or_subquery(self, ctx:SqlParser.Table_or_subqueryContext):
        pass

    # Exit a parse tree produced by SqlParser#table_or_subquery.
    def exitTable_or_subquery(self, ctx:SqlParser.Table_or_subqueryContext):
        pass


    # Enter a parse tree produced by SqlParser#join_clause.
    def enterJoin_clause(self, ctx:SqlParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by SqlParser#join_clause.
    def exitJoin_clause(self, ctx:SqlParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by SqlParser#join_operator.
    def enterJoin_operator(self, ctx:SqlParser.Join_operatorContext):
        pass

    # Exit a parse tree produced by SqlParser#join_operator.
    def exitJoin_operator(self, ctx:SqlParser.Join_operatorContext):
        pass


    # Enter a parse tree produced by SqlParser#join_constraint.
    def enterJoin_constraint(self, ctx:SqlParser.Join_constraintContext):
        pass

    # Exit a parse tree produced by SqlParser#join_constraint.
    def exitJoin_constraint(self, ctx:SqlParser.Join_constraintContext):
        pass


    # Enter a parse tree produced by SqlParser#select_core.
    def enterSelect_core(self, ctx:SqlParser.Select_coreContext):
        pass

    # Exit a parse tree produced by SqlParser#select_core.
    def exitSelect_core(self, ctx:SqlParser.Select_coreContext):
        pass


    # Enter a parse tree produced by SqlParser#compound_operator.
    def enterCompound_operator(self, ctx:SqlParser.Compound_operatorContext):
        pass

    # Exit a parse tree produced by SqlParser#compound_operator.
    def exitCompound_operator(self, ctx:SqlParser.Compound_operatorContext):
        pass


    # Enter a parse tree produced by SqlParser#cte_table_name.
    def enterCte_table_name(self, ctx:SqlParser.Cte_table_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#cte_table_name.
    def exitCte_table_name(self, ctx:SqlParser.Cte_table_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#signed_number.
    def enterSigned_number(self, ctx:SqlParser.Signed_numberContext):
        pass

    # Exit a parse tree produced by SqlParser#signed_number.
    def exitSigned_number(self, ctx:SqlParser.Signed_numberContext):
        pass


    # Enter a parse tree produced by SqlParser#literal_value.
    def enterLiteral_value(self, ctx:SqlParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by SqlParser#literal_value.
    def exitLiteral_value(self, ctx:SqlParser.Literal_valueContext):
        pass


    # Enter a parse tree produced by SqlParser#unary_operator.
    def enterUnary_operator(self, ctx:SqlParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by SqlParser#unary_operator.
    def exitUnary_operator(self, ctx:SqlParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by SqlParser#error_message.
    def enterError_message(self, ctx:SqlParser.Error_messageContext):
        pass

    # Exit a parse tree produced by SqlParser#error_message.
    def exitError_message(self, ctx:SqlParser.Error_messageContext):
        pass


    # Enter a parse tree produced by SqlParser#module_argument.
    def enterModule_argument(self, ctx:SqlParser.Module_argumentContext):
        pass

    # Exit a parse tree produced by SqlParser#module_argument.
    def exitModule_argument(self, ctx:SqlParser.Module_argumentContext):
        pass


    # Enter a parse tree produced by SqlParser#column_alias.
    def enterColumn_alias(self, ctx:SqlParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by SqlParser#column_alias.
    def exitColumn_alias(self, ctx:SqlParser.Column_aliasContext):
        pass


    # Enter a parse tree produced by SqlParser#keyword.
    def enterKeyword(self, ctx:SqlParser.KeywordContext):
        pass

    # Exit a parse tree produced by SqlParser#keyword.
    def exitKeyword(self, ctx:SqlParser.KeywordContext):
        pass


    # Enter a parse tree produced by SqlParser#unknown.
    def enterUnknown(self, ctx:SqlParser.UnknownContext):
        pass

    # Exit a parse tree produced by SqlParser#unknown.
    def exitUnknown(self, ctx:SqlParser.UnknownContext):
        pass


    # Enter a parse tree produced by SqlParser#name.
    def enterName(self, ctx:SqlParser.NameContext):
        pass

    # Exit a parse tree produced by SqlParser#name.
    def exitName(self, ctx:SqlParser.NameContext):
        pass


    # Enter a parse tree produced by SqlParser#function_name.
    def enterFunction_name(self, ctx:SqlParser.Function_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#function_name.
    def exitFunction_name(self, ctx:SqlParser.Function_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#database_name.
    def enterDatabase_name(self, ctx:SqlParser.Database_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#database_name.
    def exitDatabase_name(self, ctx:SqlParser.Database_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#source_table_name.
    def enterSource_table_name(self, ctx:SqlParser.Source_table_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#source_table_name.
    def exitSource_table_name(self, ctx:SqlParser.Source_table_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#table_name.
    def enterTable_name(self, ctx:SqlParser.Table_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#table_name.
    def exitTable_name(self, ctx:SqlParser.Table_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#table_or_index_name.
    def enterTable_or_index_name(self, ctx:SqlParser.Table_or_index_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#table_or_index_name.
    def exitTable_or_index_name(self, ctx:SqlParser.Table_or_index_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#new_table_name.
    def enterNew_table_name(self, ctx:SqlParser.New_table_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#new_table_name.
    def exitNew_table_name(self, ctx:SqlParser.New_table_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#column_name.
    def enterColumn_name(self, ctx:SqlParser.Column_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#column_name.
    def exitColumn_name(self, ctx:SqlParser.Column_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#collation_name.
    def enterCollation_name(self, ctx:SqlParser.Collation_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#collation_name.
    def exitCollation_name(self, ctx:SqlParser.Collation_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#foreign_table.
    def enterForeign_table(self, ctx:SqlParser.Foreign_tableContext):
        pass

    # Exit a parse tree produced by SqlParser#foreign_table.
    def exitForeign_table(self, ctx:SqlParser.Foreign_tableContext):
        pass


    # Enter a parse tree produced by SqlParser#index_name.
    def enterIndex_name(self, ctx:SqlParser.Index_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#index_name.
    def exitIndex_name(self, ctx:SqlParser.Index_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#trigger_name.
    def enterTrigger_name(self, ctx:SqlParser.Trigger_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#trigger_name.
    def exitTrigger_name(self, ctx:SqlParser.Trigger_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#view_name.
    def enterView_name(self, ctx:SqlParser.View_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#view_name.
    def exitView_name(self, ctx:SqlParser.View_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#module_name.
    def enterModule_name(self, ctx:SqlParser.Module_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#module_name.
    def exitModule_name(self, ctx:SqlParser.Module_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#pragma_name.
    def enterPragma_name(self, ctx:SqlParser.Pragma_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#pragma_name.
    def exitPragma_name(self, ctx:SqlParser.Pragma_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#savepoint_name.
    def enterSavepoint_name(self, ctx:SqlParser.Savepoint_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#savepoint_name.
    def exitSavepoint_name(self, ctx:SqlParser.Savepoint_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#table_alias.
    def enterTable_alias(self, ctx:SqlParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by SqlParser#table_alias.
    def exitTable_alias(self, ctx:SqlParser.Table_aliasContext):
        pass


    # Enter a parse tree produced by SqlParser#transaction_name.
    def enterTransaction_name(self, ctx:SqlParser.Transaction_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#transaction_name.
    def exitTransaction_name(self, ctx:SqlParser.Transaction_nameContext):
        pass


    # Enter a parse tree produced by SqlParser#any_name.
    def enterAny_name(self, ctx:SqlParser.Any_nameContext):
        pass

    # Exit a parse tree produced by SqlParser#any_name.
    def exitAny_name(self, ctx:SqlParser.Any_nameContext):
        pass


