create schema if not exists hawaii;
use hawaii;

create or replace table air_seats as select * from 'processed_frames/hawaii-air_seats.csv';
create or replace table expenditure_patterns as select * from 'processed_frames/hawaii-expenditure_patterns.csv';
create or replace table hotel_performance as select * from 'processed_frames/hawaii-hotel_performance.csv';
create or replace table visitor_characteristics as select * from './processed_frames/hawaii-visitor_characteristics.csv';
create or replace table visitor_trends as select * from 'processed_frames/hawaii-visitor_trends.csv';

