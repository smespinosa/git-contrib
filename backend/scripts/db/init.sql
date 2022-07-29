
create table repos
(
    id   serial primary key,
    name text
);

create table contributions
(
    id      uuid DEFAULT gen_random_uuid() PRIMARY KEY,
    repo_id integer,
    email   varchar(256),
    date    date
);

create index ix_contribution_email_date
    on contributions (email, date);