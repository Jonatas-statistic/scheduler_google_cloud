import os
import logging
import logging.config

logging.config.fileConfig('logging.ini')

logger = logging.getLogger('file')

def write_job(job:str):
    os.system(command=job)

response = input('create, update, delete or exit: ')
logger.info(f'The response is {response}')

while response not in ['create', 'update', 'delete', 'exit']:
        logger.warning(f'The response {response} is invalid!')
        response = input('create, update, delete or exit: ')

logger.info(f'The response is {response}')

# List with table names
tabelas = [
    'candidates',
    'departments',
    'gho_custom_field_values',
    'gho_custom_fields',
    'gho_employee_roles',
    'gho_employees',
    'gho_roles',
    'gho_user_activities',
    'jobs_stages',
    'interviewers',
    'opening_custom_fields',
    'scorecard_question_answers',
    'approvals',
    'scorecards_attributes',
    'offer_custom_fields',
    'demographic_free_form_answers',
    'schema_migrations',
    'gho_assigned_tasks',
    'scheduled_interviews',
    'application_stages',
    'scorecards',
    'openings',
    'application_question_answers',
    'applications_jobs',
    'agency_question_custom_fields',
    'offers',
    'eeoc_responses',
    'application_custom_fields',
    'prospect_pool_transitions',
    'rejection_question_custom_fields',
    'demographic_answers',
    'demographic_answer_option_translations',
    'candidate_survey_questions',
    'jobs_interviews',
    'stage_snapshots',
    'job_post_questions',
    'applications',
    'user_candidate_links',
    'referral_question_custom_fields',
    'candidate_custom_fields',
    'candidate_email_addresses',
    'candidate_mailing_addresses',
    'candidate_phone_numbers',
    'gdpr_consent_decisions',
    'gdpr_consent_requests',
    'candidates_tags',
    'demographic_answer_options',
    'demographic_question_translations',
    'prospect_pool_stages',
    'interviews',
    'stages',
    'jobs_departments',
    'jobs_offices',
    'job_snapshots',
    'job_custom_fields',
    'user_actions',
    'hiring_team',
    'job_posts',
    'greenhouse_usages',
    'interviewer_tags',
    'jobs_attributes',
    'referrers',
    'rejection_reasons',
    'sources',
    'events',
    'tags',
    'demographic_questions',
    'prospect_pools',
    'candidate_surveys',
    'jobs',
    'gdpr_office_rules',
    'users',
    'attributes',
    'demographic_question_sets',
    'employments',
    'offices',
    'educations',
    'organizations'
]

tabelas.sort()

if response != 'exit':
    for tabela in tabelas:
        if response == 'delete':
            job = f"gcloud scheduler jobs {response} sh-ingestion-greenhouse-{tabela} --location southamerica-east1 --quiet"
        else:
            job = f"gcloud scheduler jobs {response} http sh-ingestion-greenhouse-{tabela} --location southamerica-east1 --schedule '0 12 * * *' --time-zone 'America/Sao_Paulo' --uri 'https://api-data-ingestion-cc7qkqckgq-rj.a.run.app/greenhouse/{tabela}' --http-method GET --description 'Ingestão dos dados do greenhouse da tabela {tabela} para o datalake da Movile' --max-retry-attempts 2 --max-doublings 5"
        
        try:
            write_job(job)
            logger.info(f'Command {response} {tabela} was successfuly executed!')
        except:
            logger.error(f"Command {response} {tabela} was not successfuly execute!!!")

logger.info('--------------------- Finished! -------------------------- \n')
