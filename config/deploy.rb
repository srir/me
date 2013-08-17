set :application, "srir.me"
set :repository,  "https://github.com/srir/me.git"

set :scm, :git # You can set :scm explicitly or Capistrano will make an intelligent guess based on known version control directory names
# Or: `accurev`, `bzr`, `cvs`, `darcs`, `git`, `mercurial`, `perforce`, `subversion` or `none`

ssh_options[:user] = "srir"
ssh_options[:keys] = ["#{ENV['HOME']}/.ssh/srir"]

server "srir.me", :app, :web, primary: true
set :use_sudo, false
set :deploy_to, "/var/www/srir/me"
